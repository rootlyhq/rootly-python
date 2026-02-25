from typing import Literal, cast

IncidentStatusPageEventStatus = Literal[
    "completed", "identified", "in_progress", "investigating", "monitoring", "resolved", "scheduled"
]

INCIDENT_STATUS_PAGE_EVENT_STATUS_VALUES: set[IncidentStatusPageEventStatus] = {
    "completed",
    "identified",
    "in_progress",
    "investigating",
    "monitoring",
    "resolved",
    "scheduled",
}


def check_incident_status_page_event_status(value: str | None) -> IncidentStatusPageEventStatus | None:
    if value is None:
        return None
    if value in INCIDENT_STATUS_PAGE_EVENT_STATUS_VALUES:
        return cast(IncidentStatusPageEventStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_STATUS_PAGE_EVENT_STATUS_VALUES!r}")
