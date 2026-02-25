from typing import Literal, cast

CreateAsanaTaskTaskParamsTaskType = Literal["create_asana_task"]

CREATE_ASANA_TASK_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateAsanaTaskTaskParamsTaskType] = {
    "create_asana_task",
}


def check_create_asana_task_task_params_task_type(value: str | None) -> CreateAsanaTaskTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_ASANA_TASK_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateAsanaTaskTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_ASANA_TASK_TASK_PARAMS_TASK_TYPE_VALUES!r}")
