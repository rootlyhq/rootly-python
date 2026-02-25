from typing import Literal, cast

UpdateAlertUrgencyDataType = Literal["alert_urgencies"]

UPDATE_ALERT_URGENCY_DATA_TYPE_VALUES: set[UpdateAlertUrgencyDataType] = {
    "alert_urgencies",
}


def check_update_alert_urgency_data_type(value: str | None) -> UpdateAlertUrgencyDataType | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_URGENCY_DATA_TYPE_VALUES:
        return cast(UpdateAlertUrgencyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_URGENCY_DATA_TYPE_VALUES!r}")
