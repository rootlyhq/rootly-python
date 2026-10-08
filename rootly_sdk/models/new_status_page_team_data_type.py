from typing import Literal

NewStatusPageTeamDataType = Literal["status_page_groups"]

NEW_STATUS_PAGE_TEAM_DATA_TYPE_VALUES: set[NewStatusPageTeamDataType] = {
    "status_page_groups",
}


def check_new_status_page_team_data_type(value: str | None) -> NewStatusPageTeamDataType | None:
    if value is None:
        return None
    if value in NEW_STATUS_PAGE_TEAM_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_STATUS_PAGE_TEAM_DATA_TYPE_VALUES!r}")
