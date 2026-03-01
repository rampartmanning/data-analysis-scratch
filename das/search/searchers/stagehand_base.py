"""Browser-based web searcher using Playwright + LiteLLM (Bedrock/Nova Lite).

Instead of Stagehand's hosted service, we drive a headless browser directly
with Playwright and use LiteLLM to call Bedrock for page interpretation.
This avoids the LiteLLM proxy server complexity and Browserbase LLM key issues.
"""

import asyncio
import json
import os
import time

from das.search.searchers.base import MarketplaceSearcher
from das.search.config import SearchConfig
from das.search.models import SearchResult, SearchStatus, MarketplaceMatch


async def _extract_with_llm(page_text: str, instruction: str, schema: dict, config: SearchConfig) -> dict:
    """Use LiteLLM to extract structured data from page text content."""
    import litellm

    os.environ["AWS_PROFILE"] = config.aws_profile
    # Truncate to avoid token limits — body text is much more compact than HTML
    text_truncated = page_text[:15000]

    prompt = f"""You are extracting structured data from a web page's text content.

Instruction: {instruction}

Return ONLY valid JSON matching this schema:
{json.dumps(schema, indent=2)}

If no results are found, return: {{"results": []}}

Page text:
{text_truncated}"""

    resp = await asyncio.to_thread(
        litellm.completion,
        model=config.stagehand_model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=4000,
        aws_region_name="us-east-1",
    )

    text = resp.choices[0].message.content.strip()
    # Strip markdown code fences if present
    if text.startswith("```"):
        text = text.split("\n", 1)[1] if "\n" in text else text[3:]
    if text.endswith("```"):
        text = text[:-3]
    if text.startswith("json"):
        text = text[4:]
    text = text.strip()

    # Try to find JSON object in the response even if there's extra text
    start_idx = text.find("{")
    end_idx = text.rfind("}")
    if start_idx != -1 and end_idx != -1:
        text = text[start_idx:end_idx + 1]

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Common LLM failures: trailing commas, truncated output
        import re
        cleaned = re.sub(r',\s*([}\]])', r'\1', text)
        return json.loads(cleaned)


class _BrowserPool:
    """Shared Playwright browser instance across all Tier 2 searchers."""

    _instance: "_BrowserPool | None" = None
    _lock = asyncio.Lock()

    def __init__(self):
        self._playwright = None
        self._browser = None

    @classmethod
    async def get(cls) -> "_BrowserPool":
        async with cls._lock:
            if cls._instance is not None and cls._instance._browser:
                return cls._instance
            pool = cls()
            await pool._start()
            cls._instance = pool
            return pool

    async def _start(self):
        from playwright.async_api import async_playwright
        self._playwright = await async_playwright().start()
        self._browser = await self._playwright.chromium.launch(headless=True)

    async def new_page(self):
        return await self._browser.new_page()

    @classmethod
    async def shutdown(cls):
        async with cls._lock:
            if cls._instance:
                if cls._instance._browser:
                    await cls._instance._browser.close()
                if cls._instance._playwright:
                    await cls._instance._playwright.stop()
                cls._instance = None


class StagehandSearcher(MarketplaceSearcher):
    """Base class for Tier 2 web-scraping searchers.

    Uses Playwright for browser automation + LiteLLM/Bedrock for page interpretation.

    Subclasses set:
        - url: str — marketplace search URL (use {query} placeholder)
        - extract_instructions: str — what to extract from the results page
        - extract_schema: dict — JSON schema for structured extraction
    """

    tier = 2
    url: str = ""
    search_instructions: str = ""
    extract_instructions: str = ""
    extract_schema: dict = {}

    async def search(self, query: str, *, config: SearchConfig) -> SearchResult:
        start = time.time()
        try:
            matches = await self._browser_search(query, config)
        except Exception as e:
            return SearchResult(
                marketplace=self.name, status=SearchStatus.ERROR,
                error=str(e)[:200], elapsed_seconds=time.time() - start, tier=self.tier,
            )
        elapsed = time.time() - start

        if not matches:
            return SearchResult(marketplace=self.name, status=SearchStatus.NOT_FOUND,
                                elapsed_seconds=elapsed, tier=self.tier)

        return SearchResult(
            marketplace=self.name, status=SearchStatus.FOUND,
            hits=len(matches), matches=matches[:10],
            elapsed_seconds=elapsed, tier=self.tier,
        )

    async def _browser_search(self, query: str, config: SearchConfig) -> list[MarketplaceMatch]:
        pool = await _BrowserPool.get()
        page = await pool.new_page()

        try:
            # Navigate to search URL
            nav_url = self.url.replace("{query}", query)
            await page.goto(nav_url, wait_until="domcontentloaded", timeout=20000)

            # If search_instructions say to type into search box, do it
            if "{query}" not in self.url:
                await self._perform_search(page, query)

            # Wait for results to load
            await page.wait_for_timeout(3000)

            # Get page text (much more compact than raw HTML)
            page_text = await page.inner_text("body")

            # Extract results using LLM
            data = await _extract_with_llm(page_text, self.extract_instructions, self.extract_schema, config)

            results = data.get("results", [])
            return [
                MarketplaceMatch(
                    title=r.get("title", "Untitled")[:100],
                    url=r.get("url", ""),
                    description=r.get("description", "")[:200],
                    provider=r.get("provider", ""),
                    pricing=r.get("pricing", ""),
                )
                for r in results
                if isinstance(r, dict) and r.get("title")
            ]
        finally:
            await page.close()

    async def _perform_search(self, page, query: str):
        """Type query into search box and submit. Override for custom behavior."""
        # Try common search selectors
        for selector in [
            'input[type="search"]',
            'input[name="q"]',
            'input[name="query"]',
            'input[name="search"]',
            'input[placeholder*="earch"]',
            'input[aria-label*="earch"]',
            "input.search",
            "#search",
            "#search-input",
        ]:
            try:
                el = page.locator(selector).first
                if await el.is_visible(timeout=2000):
                    await el.fill(query)
                    await el.press("Enter")
                    return
            except Exception:
                continue

        # Fallback: try the first visible text input
        try:
            inputs = page.locator('input[type="text"]')
            count = await inputs.count()
            for i in range(min(count, 3)):
                el = inputs.nth(i)
                if await el.is_visible():
                    await el.fill(query)
                    await el.press("Enter")
                    return
        except Exception:
            pass
