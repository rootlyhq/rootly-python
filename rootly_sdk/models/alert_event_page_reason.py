from typing import Literal

AlertEventPageReason = Literal["manual_reassignment"]

ALERT_EVENT_PAGE_REASON_VALUES: set[AlertEventPageReason] = {
    "manual_reassignment",
}


def check_alert_event_page_reason(value: str | None) -> AlertEventPageReason | None:
    if value is None:
        return None
    if value in ALERT_EVENT_PAGE_REASON_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_EVENT_PAGE_REASON_VALUES!r}")
