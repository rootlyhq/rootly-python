from typing import Literal, cast

NewAlertUrgencyDataType = Literal["alert_urgencies"]

NEW_ALERT_URGENCY_DATA_TYPE_VALUES: set[NewAlertUrgencyDataType] = {
    "alert_urgencies",
}


def check_new_alert_urgency_data_type(value: str | None) -> NewAlertUrgencyDataType | None:
    if value is None:
        return None
    if value in NEW_ALERT_URGENCY_DATA_TYPE_VALUES:
        return cast(NewAlertUrgencyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_ALERT_URGENCY_DATA_TYPE_VALUES!r}")
