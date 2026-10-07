from typing import Literal

AddTeamTaskParamsTaskType = Literal["add_team"]

ADD_TEAM_TASK_PARAMS_TASK_TYPE_VALUES: set[AddTeamTaskParamsTaskType] = {
    "add_team",
}


def check_add_team_task_params_task_type(value: str | None) -> AddTeamTaskParamsTaskType | None:
    if value is None:
        return None
    if value in ADD_TEAM_TASK_PARAMS_TASK_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ADD_TEAM_TASK_PARAMS_TASK_TYPE_VALUES!r}")
