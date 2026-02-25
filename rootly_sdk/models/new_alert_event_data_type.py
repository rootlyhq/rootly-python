from typing import Literal, cast

NewAlertEventDataType = Literal["alert_events"]

NEW_ALERT_EVENT_DATA_TYPE_VALUES: set[NewAlertEventDataType] = {
    "alert_events",
}


def check_new_alert_event_data_type(value: str | None) -> NewAlertEventDataType | None:
    if value is None:
        return None
    if value in NEW_ALERT_EVENT_DATA_TYPE_VALUES:
        return cast(NewAlertEventDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_ALERT_EVENT_DATA_TYPE_VALUES!r}")
