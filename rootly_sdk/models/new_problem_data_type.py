from typing import Literal

NewProblemDataType = Literal["problems"]

NEW_PROBLEM_DATA_TYPE_VALUES: set[NewProblemDataType] = {
    "problems",
}


def check_new_problem_data_type(value: str | None) -> NewProblemDataType | None:
    if value is None:
        return None
    if value in NEW_PROBLEM_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_PROBLEM_DATA_TYPE_VALUES!r}")
