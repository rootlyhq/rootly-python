from typing import Literal, cast

AlertEventResponseDataType = Literal["alert_events"]

ALERT_EVENT_RESPONSE_DATA_TYPE_VALUES: set[AlertEventResponseDataType] = {
    "alert_events",
}


def check_alert_event_response_data_type(value: str | None) -> AlertEventResponseDataType | None:
    if value is None:
        return None
    if value in ALERT_EVENT_RESPONSE_DATA_TYPE_VALUES:
        return cast(AlertEventResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_EVENT_RESPONSE_DATA_TYPE_VALUES!r}")
