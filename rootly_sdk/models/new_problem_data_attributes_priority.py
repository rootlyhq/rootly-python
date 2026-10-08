from typing import Literal

NewProblemDataAttributesPriority = Literal["P0", "P1", "P2", "P3"]

NEW_PROBLEM_DATA_ATTRIBUTES_PRIORITY_VALUES: set[NewProblemDataAttributesPriority] = {
    "P0",
    "P1",
    "P2",
    "P3",
}


def check_new_problem_data_attributes_priority(value: str | None) -> NewProblemDataAttributesPriority | None:
    if value is None:
        return None
    if value in NEW_PROBLEM_DATA_ATTRIBUTES_PRIORITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_PROBLEM_DATA_ATTRIBUTES_PRIORITY_VALUES!r}")
