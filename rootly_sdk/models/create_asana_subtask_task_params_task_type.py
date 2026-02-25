from typing import Literal, cast

CreateAsanaSubtaskTaskParamsTaskType = Literal["create_asana_subtask"]

CREATE_ASANA_SUBTASK_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateAsanaSubtaskTaskParamsTaskType] = {
    "create_asana_subtask",
}


def check_create_asana_subtask_task_params_task_type(value: str | None) -> CreateAsanaSubtaskTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_ASANA_SUBTASK_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateAsanaSubtaskTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_ASANA_SUBTASK_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
