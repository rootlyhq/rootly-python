from typing import Literal

UpdateProblemDataType = Literal["problems"]

UPDATE_PROBLEM_DATA_TYPE_VALUES: set[UpdateProblemDataType] = {
    "problems",
}


def check_update_problem_data_type(value: str | None) -> UpdateProblemDataType | None:
    if value is None:
        return None
    if value in UPDATE_PROBLEM_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_PROBLEM_DATA_TYPE_VALUES!r}")
