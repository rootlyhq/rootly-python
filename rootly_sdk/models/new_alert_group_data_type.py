from typing import Literal, cast

NewAlertGroupDataType = Literal["alert_groups"]

NEW_ALERT_GROUP_DATA_TYPE_VALUES: set[NewAlertGroupDataType] = {
    "alert_groups",
}


def check_new_alert_group_data_type(value: str | None) -> NewAlertGroupDataType | None:
    if value is None:
        return None
    if value in NEW_ALERT_GROUP_DATA_TYPE_VALUES:
        return cast(NewAlertGroupDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_ALERT_GROUP_DATA_TYPE_VALUES!r}")
