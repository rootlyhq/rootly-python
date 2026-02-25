from typing import Literal, cast

UpdateAsanaTaskTaskParamsDependencyDirection = Literal["blocked_by", "blocking"]

UPDATE_ASANA_TASK_TASK_PARAMS_DEPENDENCY_DIRECTION_VALUES: set[UpdateAsanaTaskTaskParamsDependencyDirection] = {
    "blocked_by",
    "blocking",
}


def check_update_asana_task_task_params_dependency_direction(
    value: str | None,
) -> UpdateAsanaTaskTaskParamsDependencyDirection | None:
    if value is None:
        return None
    if value in UPDATE_ASANA_TASK_TASK_PARAMS_DEPENDENCY_DIRECTION_VALUES:
        return cast(UpdateAsanaTaskTaskParamsDependencyDirection, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ASANA_TASK_TASK_PARAMS_DEPENDENCY_DIRECTION_VALUES!r}"
    )
