from typing import Literal, cast

AlertUrgencyListDataItemType = Literal["alert_urgencies"]

ALERT_URGENCY_LIST_DATA_ITEM_TYPE_VALUES: set[AlertUrgencyListDataItemType] = {
    "alert_urgencies",
}


def check_alert_urgency_list_data_item_type(value: str | None) -> AlertUrgencyListDataItemType | None:
    if value is None:
        return None
    if value in ALERT_URGENCY_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(AlertUrgencyListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_URGENCY_LIST_DATA_ITEM_TYPE_VALUES!r}")
