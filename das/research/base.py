"""Base class for research tasks with built-in checkpoint/resume."""

from abc import ABC, abstractmethod
from das.utils.progress import save_checkpoint, load_checkpoint, clear_checkpoint


class ResearchTask(ABC):
    """Subclass this to create a resumable research task.

    Implement `run()` to do the work. Call `self.save(state)` periodically
    so work can resume on interruption. `self.prior_state` holds the last
    checkpoint (or None on first run).
    """

    def __init__(self, task_id: str):
        self.task_id = task_id
        self.prior_state = load_checkpoint(task_id)

    def save(self, state: dict):
        save_checkpoint(self.task_id, state)

    def done(self, final_state: dict | None = None):
        if final_state:
            final_state["_completed"] = True
            save_checkpoint(self.task_id, final_state)
        else:
            clear_checkpoint(self.task_id)

    @abstractmethod
    def run(self):
        ...
