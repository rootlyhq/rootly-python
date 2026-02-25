from typing import Literal, cast

GetTeamInclude = Literal["users"]

GET_TEAM_INCLUDE_VALUES: set[GetTeamInclude] = {
    "users",
}


def check_get_team_include(value: str | None) -> GetTeamInclude | None:
    if value is None:
        return None
    if value in GET_TEAM_INCLUDE_VALUES:
        return cast(GetTeamInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_TEAM_INCLUDE_VALUES!r}")
