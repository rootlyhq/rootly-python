from typing import Literal

ProblemStatus = Literal["cancelled", "completed", "created", "deferred", "in_progress"]

PROBLEM_STATUS_VALUES: set[ProblemStatus] = {
    "cancelled",
    "completed",
    "created",
    "deferred",
    "in_progress",
}


def check_problem_status(value: str | None) -> ProblemStatus | None:
    if value is None:
        return None
    if value in PROBLEM_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROBLEM_STATUS_VALUES!r}")
