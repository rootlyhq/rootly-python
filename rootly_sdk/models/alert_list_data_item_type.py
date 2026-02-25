from typing import Literal, cast

AlertListDataItemType = Literal["alerts"]

ALERT_LIST_DATA_ITEM_TYPE_VALUES: set[AlertListDataItemType] = {
    "alerts",
}


def check_alert_list_data_item_type(value: str | None) -> AlertListDataItemType | None:
    if value is None:
        return None
    if value in ALERT_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(AlertListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_LIST_DATA_ITEM_TYPE_VALUES!r}")
