from typing import Literal

TeamListDataItemType = Literal["groups"]

TEAM_LIST_DATA_ITEM_TYPE_VALUES: set[TeamListDataItemType] = {
    "groups",
}


def check_team_list_data_item_type(value: str | None) -> TeamListDataItemType | None:
    if value is None:
        return None
    if value in TEAM_LIST_DATA_ITEM_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEAM_LIST_DATA_ITEM_TYPE_VALUES!r}")
