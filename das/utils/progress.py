"""Checkpoint/resume support for long-running research tasks.

Saves progress to tmp/progress/ so work can resume after interruption.
"""

import json
import os
from pathlib import Path
from datetime import datetime, timezone

TMP_DIR = Path(__file__).resolve().parent.parent.parent / "tmp"
PROGRESS_DIR = TMP_DIR / "progress"
CACHE_DIR = TMP_DIR / "cache"


def _ensure_dirs():
    PROGRESS_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)


def checkpoint_path(task_id: str) -> Path:
    _ensure_dirs()
    return PROGRESS_DIR / f"{task_id}.json"


def save_checkpoint(task_id: str, state: dict):
    """Save task state to disk so it can be resumed."""
    _ensure_dirs()
    state["_checkpoint_ts"] = datetime.now(timezone.utc).isoformat()
    path = checkpoint_path(task_id)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2, default=str))
    tmp.rename(path)  # atomic on same filesystem


def load_checkpoint(task_id: str) -> dict | None:
    """Load saved state, or None if no checkpoint exists."""
    path = checkpoint_path(task_id)
    if path.exists():
        return json.loads(path.read_text())
    return None


def clear_checkpoint(task_id: str):
    path = checkpoint_path(task_id)
    if path.exists():
        path.unlink()


def list_checkpoints() -> list[str]:
    _ensure_dirs()
    return [p.stem for p in PROGRESS_DIR.glob("*.json")]
