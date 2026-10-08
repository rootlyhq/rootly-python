from typing import Literal

UpdateProblemDataAttributesPriority = Literal["P0", "P1", "P2", "P3"]

UPDATE_PROBLEM_DATA_ATTRIBUTES_PRIORITY_VALUES: set[UpdateProblemDataAttributesPriority] = {
    "P0",
    "P1",
    "P2",
    "P3",
}


def check_update_problem_data_attributes_priority(value: str | None) -> UpdateProblemDataAttributesPriority | None:
    if value is None:
        return None
    if value in UPDATE_PROBLEM_DATA_ATTRIBUTES_PRIORITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_PROBLEM_DATA_ATTRIBUTES_PRIORITY_VALUES!r}")
