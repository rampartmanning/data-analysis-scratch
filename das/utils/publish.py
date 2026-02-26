"""Publish research findings as static JSON consumed by the Vue3 UI."""

import json
from pathlib import Path
from datetime import datetime, timezone

UI_DIST = Path(__file__).resolve().parent.parent.parent / "ui" / "public" / "data"


def publish_findings(topic: str, findings: list[dict], metadata: dict | None = None):
    """Write findings to a JSON file the UI can load."""
    UI_DIST.mkdir(parents=True, exist_ok=True)

    payload = {
        "topic": topic,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "metadata": metadata or {},
        "findings": findings,
    }

    out = UI_DIST / f"{_slug(topic)}.json"
    out.write_text(json.dumps(payload, indent=2, default=str))

    # Update the manifest so the UI knows what topics exist
    _update_manifest(topic, out.name)
    return out


def _update_manifest(topic: str, filename: str):
    manifest_path = UI_DIST / "manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
    else:
        manifest = {"topics": []}

    # Upsert
    existing = {t["filename"]: t for t in manifest["topics"]}
    existing[filename] = {
        "topic": topic,
        "filename": filename,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    manifest["topics"] = list(existing.values())
    manifest_path.write_text(json.dumps(manifest, indent=2))


def _slug(text: str) -> str:
    return text.lower().replace(" ", "-").replace("/", "-")[:60]
