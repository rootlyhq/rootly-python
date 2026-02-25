from typing import Literal, cast

CreateClickupTaskTaskParamsTaskType = Literal["create_clickup_task"]

CREATE_CLICKUP_TASK_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateClickupTaskTaskParamsTaskType] = {
    "create_clickup_task",
}


def check_create_clickup_task_task_params_task_type(value: str | None) -> CreateClickupTaskTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_CLICKUP_TASK_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateClickupTaskTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_CLICKUP_TASK_TASK_PARAMS_TASK_TYPE_VALUES!r}")
