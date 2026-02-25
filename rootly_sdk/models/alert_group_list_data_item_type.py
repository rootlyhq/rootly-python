from typing import Literal, cast

AlertGroupListDataItemType = Literal["alert_groups"]

ALERT_GROUP_LIST_DATA_ITEM_TYPE_VALUES: set[AlertGroupListDataItemType] = {
    "alert_groups",
}


def check_alert_group_list_data_item_type(value: str | None) -> AlertGroupListDataItemType | None:
    if value is None:
        return None
    if value in ALERT_GROUP_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(AlertGroupListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_GROUP_LIST_DATA_ITEM_TYPE_VALUES!r}")
