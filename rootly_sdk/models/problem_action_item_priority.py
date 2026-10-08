from typing import Literal

ProblemActionItemPriority = Literal["high", "low", "medium"]

PROBLEM_ACTION_ITEM_PRIORITY_VALUES: set[ProblemActionItemPriority] = {
    "high",
    "low",
    "medium",
}


def check_problem_action_item_priority(value: str | None) -> ProblemActionItemPriority | None:
    if value is None:
        return None
    if value in PROBLEM_ACTION_ITEM_PRIORITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROBLEM_ACTION_ITEM_PRIORITY_VALUES!r}")
