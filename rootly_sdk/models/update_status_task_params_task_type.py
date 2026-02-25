from typing import Literal, cast

UpdateStatusTaskParamsTaskType = Literal["update_status"]

UPDATE_STATUS_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateStatusTaskParamsTaskType] = {
    "update_status",
}


def check_update_status_task_params_task_type(value: str | None) -> UpdateStatusTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_STATUS_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateStatusTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_STATUS_TASK_PARAMS_TASK_TYPE_VALUES!r}")
