from typing import Literal

ProblemActionItemStatus = Literal["cancelled", "done", "in_progress", "open"]

PROBLEM_ACTION_ITEM_STATUS_VALUES: set[ProblemActionItemStatus] = {
    "cancelled",
    "done",
    "in_progress",
    "open",
}


def check_problem_action_item_status(value: str | None) -> ProblemActionItemStatus | None:
    if value is None:
        return None
    if value in PROBLEM_ACTION_ITEM_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROBLEM_ACTION_ITEM_STATUS_VALUES!r}")
