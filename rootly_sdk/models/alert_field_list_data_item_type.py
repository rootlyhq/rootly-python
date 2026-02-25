from typing import Literal, cast

AlertFieldListDataItemType = Literal["alert_fields"]

ALERT_FIELD_LIST_DATA_ITEM_TYPE_VALUES: set[AlertFieldListDataItemType] = {
    "alert_fields",
}


def check_alert_field_list_data_item_type(value: str | None) -> AlertFieldListDataItemType | None:
    if value is None:
        return None
    if value in ALERT_FIELD_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(AlertFieldListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_FIELD_LIST_DATA_ITEM_TYPE_VALUES!r}")
