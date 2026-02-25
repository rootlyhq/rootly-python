from typing import Literal, cast

ListTeamsInclude = Literal["users"]

LIST_TEAMS_INCLUDE_VALUES: set[ListTeamsInclude] = {
    "users",
}


def check_list_teams_include(value: str | None) -> ListTeamsInclude | None:
    if value is None:
        return None
    if value in LIST_TEAMS_INCLUDE_VALUES:
        return cast(ListTeamsInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_TEAMS_INCLUDE_VALUES!r}")
