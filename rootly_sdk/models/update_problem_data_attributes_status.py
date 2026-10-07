from typing import Literal

UpdateProblemDataAttributesStatus = Literal["cancelled", "completed", "created", "deferred", "in_progress"]

UPDATE_PROBLEM_DATA_ATTRIBUTES_STATUS_VALUES: set[UpdateProblemDataAttributesStatus] = {
    "cancelled",
    "completed",
    "created",
    "deferred",
    "in_progress",
}


def check_update_problem_data_attributes_status(value: str | None) -> UpdateProblemDataAttributesStatus | None:
    if value is None:
        return None
    if value in UPDATE_PROBLEM_DATA_ATTRIBUTES_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_PROBLEM_DATA_ATTRIBUTES_STATUS_VALUES!r}")
