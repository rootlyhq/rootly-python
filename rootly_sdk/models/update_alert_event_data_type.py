from typing import Literal, cast

UpdateAlertEventDataType = Literal["alert_events"]

UPDATE_ALERT_EVENT_DATA_TYPE_VALUES: set[UpdateAlertEventDataType] = {
    "alert_events",
}


def check_update_alert_event_data_type(value: str | None) -> UpdateAlertEventDataType | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_EVENT_DATA_TYPE_VALUES:
        return cast(UpdateAlertEventDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_EVENT_DATA_TYPE_VALUES!r}")
