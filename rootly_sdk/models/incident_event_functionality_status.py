from typing import Literal, cast

IncidentEventFunctionalityStatus = Literal["major_outage", "operational", "partial_outage"]

INCIDENT_EVENT_FUNCTIONALITY_STATUS_VALUES: set[IncidentEventFunctionalityStatus] = {
    "major_outage",
    "operational",
    "partial_outage",
}


def check_incident_event_functionality_status(value: str | None) -> IncidentEventFunctionalityStatus | None:
    if value is None:
        return None
    if value in INCIDENT_EVENT_FUNCTIONALITY_STATUS_VALUES:
        return cast(IncidentEventFunctionalityStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_EVENT_FUNCTIONALITY_STATUS_VALUES!r}")
