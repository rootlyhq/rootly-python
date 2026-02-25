from typing import Literal, cast

CreateAsanaTaskTaskParamsDependencyDirection = Literal["blocked_by", "blocking"]

CREATE_ASANA_TASK_TASK_PARAMS_DEPENDENCY_DIRECTION_VALUES: set[CreateAsanaTaskTaskParamsDependencyDirection] = {
    "blocked_by",
    "blocking",
}


def check_create_asana_task_task_params_dependency_direction(
    value: str | None,
) -> CreateAsanaTaskTaskParamsDependencyDirection | None:
    if value is None:
        return None
    if value in CREATE_ASANA_TASK_TASK_PARAMS_DEPENDENCY_DIRECTION_VALUES:
        return cast(CreateAsanaTaskTaskParamsDependencyDirection, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_ASANA_TASK_TASK_PARAMS_DEPENDENCY_DIRECTION_VALUES!r}"
    )
