from typing import Literal

StatusPageTeamResponseDataType = Literal["status_page_groups"]

STATUS_PAGE_TEAM_RESPONSE_DATA_TYPE_VALUES: set[StatusPageTeamResponseDataType] = {
    "status_page_groups",
}


def check_status_page_team_response_data_type(value: str | None) -> StatusPageTeamResponseDataType | None:
    if value is None:
        return None
    if value in STATUS_PAGE_TEAM_RESPONSE_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_TEAM_RESPONSE_DATA_TYPE_VALUES!r}")
