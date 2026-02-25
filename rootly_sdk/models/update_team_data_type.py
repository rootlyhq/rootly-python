from typing import Literal, cast

UpdateTeamDataType = Literal["groups"]

UPDATE_TEAM_DATA_TYPE_VALUES: set[UpdateTeamDataType] = {
    "groups",
}


def check_update_team_data_type(value: str | None) -> UpdateTeamDataType | None:
    if value is None:
        return None
    if value in UPDATE_TEAM_DATA_TYPE_VALUES:
        return cast(UpdateTeamDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_TEAM_DATA_TYPE_VALUES!r}")
