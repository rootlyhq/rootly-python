from typing import Literal

StatusPageTeamListDataItemType = Literal["status_page_groups"]

STATUS_PAGE_TEAM_LIST_DATA_ITEM_TYPE_VALUES: set[StatusPageTeamListDataItemType] = {
    "status_page_groups",
}


def check_status_page_team_list_data_item_type(value: str | None) -> StatusPageTeamListDataItemType | None:
    if value is None:
        return None
    if value in STATUS_PAGE_TEAM_LIST_DATA_ITEM_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_TEAM_LIST_DATA_ITEM_TYPE_VALUES!r}")
