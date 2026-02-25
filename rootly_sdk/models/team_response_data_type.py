from typing import Literal, cast

TeamResponseDataType = Literal["groups"]

TEAM_RESPONSE_DATA_TYPE_VALUES: set[TeamResponseDataType] = {
    "groups",
}


def check_team_response_data_type(value: str | None) -> TeamResponseDataType | None:
    if value is None:
        return None
    if value in TEAM_RESPONSE_DATA_TYPE_VALUES:
        return cast(TeamResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEAM_RESPONSE_DATA_TYPE_VALUES!r}")
