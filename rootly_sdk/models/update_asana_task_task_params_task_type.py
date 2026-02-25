from typing import Literal, cast

UpdateAsanaTaskTaskParamsTaskType = Literal["update_asana_task"]

UPDATE_ASANA_TASK_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateAsanaTaskTaskParamsTaskType] = {
    "update_asana_task",
}


def check_update_asana_task_task_params_task_type(value: str | None) -> UpdateAsanaTaskTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_ASANA_TASK_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateAsanaTaskTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ASANA_TASK_TASK_PARAMS_TASK_TYPE_VALUES!r}")
