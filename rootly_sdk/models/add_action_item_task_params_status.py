from enum import Enum


class AddActionItemTaskParamsStatus(str, Enum):
    CANCELLED = "cancelled"
    DONE = "done"
    IN_PROGRESS = "in_progress"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
