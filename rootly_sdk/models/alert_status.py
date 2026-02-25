from typing import Literal, cast

AlertStatus = Literal["acknowledged", "deferred", "open", "resolved", "triggered"]

ALERT_STATUS_VALUES: set[AlertStatus] = {
    "acknowledged",
    "deferred",
    "open",
    "resolved",
    "triggered",
}


def check_alert_status(value: str | None) -> AlertStatus | None:
    if value is None:
        return None
    if value in ALERT_STATUS_VALUES:
        return cast(AlertStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_STATUS_VALUES!r}")
