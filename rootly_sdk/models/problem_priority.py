from typing import Literal

ProblemPriority = Literal["P0", "P1", "P2", "P3"]

PROBLEM_PRIORITY_VALUES: set[ProblemPriority] = {
    "P0",
    "P1",
    "P2",
    "P3",
}


def check_problem_priority(value: str | None) -> ProblemPriority | None:
    if value is None:
        return None
    if value in PROBLEM_PRIORITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROBLEM_PRIORITY_VALUES!r}")
