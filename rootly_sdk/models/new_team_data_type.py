from typing import Literal, cast

NewTeamDataType = Literal["groups"]

NEW_TEAM_DATA_TYPE_VALUES: set[NewTeamDataType] = {
    "groups",
}


def check_new_team_data_type(value: str | None) -> NewTeamDataType | None:
    if value is None:
        return None
    if value in NEW_TEAM_DATA_TYPE_VALUES:
        return cast(NewTeamDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_TEAM_DATA_TYPE_VALUES!r}")
