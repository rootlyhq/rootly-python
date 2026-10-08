from typing import Literal

GetTeamInclude = Literal["escalation_policies", "schedules", "users"]

GET_TEAM_INCLUDE_VALUES: set[GetTeamInclude] = {
    "escalation_policies",
    "schedules",
    "users",
}


def check_get_team_include(value: str | None) -> GetTeamInclude | None:
    if value is None:
        return None
    if value in GET_TEAM_INCLUDE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_TEAM_INCLUDE_VALUES!r}")
