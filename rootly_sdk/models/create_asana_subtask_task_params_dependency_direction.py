from typing import Literal, cast

CreateAsanaSubtaskTaskParamsDependencyDirection = Literal["blocked_by", "blocking"]

CREATE_ASANA_SUBTASK_TASK_PARAMS_DEPENDENCY_DIRECTION_VALUES: set[CreateAsanaSubtaskTaskParamsDependencyDirection] = {
    "blocked_by",
    "blocking",
}


def check_create_asana_subtask_task_params_dependency_direction(
    value: str | None,
) -> CreateAsanaSubtaskTaskParamsDependencyDirection | None:
    if value is None:
        return None
    if value in CREATE_ASANA_SUBTASK_TASK_PARAMS_DEPENDENCY_DIRECTION_VALUES:
        return cast(CreateAsanaSubtaskTaskParamsDependencyDirection, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_ASANA_SUBTASK_TASK_PARAMS_DEPENDENCY_DIRECTION_VALUES!r}"
    )
