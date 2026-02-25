from typing import Literal, cast

AlertsSourceStatus = Literal["connected", "setup_complete", "setup_incomplete"]

ALERTS_SOURCE_STATUS_VALUES: set[AlertsSourceStatus] = {
    "connected",
    "setup_complete",
    "setup_incomplete",
}


def check_alerts_source_status(value: str | None) -> AlertsSourceStatus | None:
    if value is None:
        return None
    if value in ALERTS_SOURCE_STATUS_VALUES:
        return cast(AlertsSourceStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERTS_SOURCE_STATUS_VALUES!r}")
