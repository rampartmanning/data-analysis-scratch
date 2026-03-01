"""FastAPI server bridging the Vue3 UI to the search orchestrator via SSE."""

import asyncio
import json
import time

from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse

from das.search.config import load_config
from das.search.models import SearchResult
from das.search.orchestrator import run_search
from das.search.report import write_report
from das.search.searchers import TIER1_SEARCHERS, TIER2_SEARCHERS, ALL_SEARCHERS

app = FastAPI(title="DAS Search API")

# Single-user lock — only one search at a time
_search_lock = asyncio.Lock()


def _sse_event(event: str, data: dict) -> str:
    return f"event: {event}\ndata: {json.dumps(data)}\n\n"


@app.get("/api/marketplaces")
async def list_marketplaces():
    """Return all marketplace names with their tiers."""
    results = []
    for cls in ALL_SEARCHERS:
        s = cls()
        results.append({"name": s.name, "tier": s.tier})
    return results


@app.get("/api/search")
async def search(q: str = Query(..., min_length=1), api_only: bool = False):
    """Stream search results as SSE events."""
    if _search_lock.locked():
        return StreamingResponse(
            iter([json.dumps({"error": "A search is already running"})]),
            status_code=409,
            media_type="application/json",
        )

    async def event_stream():
        async with _search_lock:
            config = load_config()
            queue: asyncio.Queue[SearchResult | None] = asyncio.Queue()

            # Determine total marketplaces
            total = len(TIER1_SEARCHERS)
            if not api_only:
                total += len(TIER2_SEARCHERS)

            # Send start event
            yield _sse_event("search:start", {
                "query": q,
                "total_marketplaces": total,
                "api_only": api_only,
            })

            completed_count = 0
            start = time.time()

            def on_result(result: SearchResult):
                queue.put_nowait(result)

            # Launch the search as a background task
            search_task = asyncio.create_task(
                run_search(
                    query=q,
                    config=config,
                    api_only=api_only,
                    on_result=on_result,
                    quiet=True,
                )
            )

            # Stream results as they arrive
            while True:
                # Wait for a result or check if search is done
                done_waiting = False
                while not done_waiting:
                    try:
                        result = queue.get_nowait()
                        completed_count += 1
                        payload = result.to_dict()
                        payload["progress"] = {
                            "completed": completed_count,
                            "total": total,
                        }
                        yield _sse_event("search:result", payload)
                        done_waiting = True
                    except asyncio.QueueEmpty:
                        if search_task.done():
                            done_waiting = True
                        else:
                            # Send keepalive and wait briefly
                            yield ": keepalive\n\n"
                            await asyncio.sleep(0.5)

                if search_task.done():
                    # Drain any remaining results
                    while not queue.empty():
                        result = queue.get_nowait()
                        completed_count += 1
                        payload = result.to_dict()
                        payload["progress"] = {
                            "completed": completed_count,
                            "total": total,
                        }
                        yield _sse_event("search:result", payload)
                    break

            elapsed = time.time() - start
            results = search_task.result()

            # Write markdown report
            report_path = write_report(q, results, elapsed)

            yield _sse_event("search:complete", {
                "query": q,
                "elapsed_seconds": round(elapsed, 1),
                "total_results": sum(r.hits for r in results),
                "report_path": str(report_path),
            })

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
