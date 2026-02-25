from typing import Literal, cast

UpdateAlertGroupDataType = Literal["alert_groups"]

UPDATE_ALERT_GROUP_DATA_TYPE_VALUES: set[UpdateAlertGroupDataType] = {
    "alert_groups",
}


def check_update_alert_group_data_type(value: str | None) -> UpdateAlertGroupDataType | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_GROUP_DATA_TYPE_VALUES:
        return cast(UpdateAlertGroupDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_GROUP_DATA_TYPE_VALUES!r}")
