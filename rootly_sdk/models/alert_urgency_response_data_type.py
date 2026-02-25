from typing import Literal, cast

AlertUrgencyResponseDataType = Literal["alert_urgencies"]

ALERT_URGENCY_RESPONSE_DATA_TYPE_VALUES: set[AlertUrgencyResponseDataType] = {
    "alert_urgencies",
}


def check_alert_urgency_response_data_type(value: str | None) -> AlertUrgencyResponseDataType | None:
    if value is None:
        return None
    if value in ALERT_URGENCY_RESPONSE_DATA_TYPE_VALUES:
        return cast(AlertUrgencyResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_URGENCY_RESPONSE_DATA_TYPE_VALUES!r}")
