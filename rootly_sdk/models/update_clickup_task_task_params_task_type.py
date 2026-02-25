from typing import Literal, cast

UpdateClickupTaskTaskParamsTaskType = Literal["update_clickup_task"]

UPDATE_CLICKUP_TASK_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateClickupTaskTaskParamsTaskType] = {
    "update_clickup_task",
}


def check_update_clickup_task_task_params_task_type(value: str | None) -> UpdateClickupTaskTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_CLICKUP_TASK_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateClickupTaskTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_CLICKUP_TASK_TASK_PARAMS_TASK_TYPE_VALUES!r}")
