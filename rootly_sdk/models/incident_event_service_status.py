from typing import Literal, cast

IncidentEventServiceStatus = Literal["major_outage", "operational", "partial_outage"]

INCIDENT_EVENT_SERVICE_STATUS_VALUES: set[IncidentEventServiceStatus] = {
    "major_outage",
    "operational",
    "partial_outage",
}


def check_incident_event_service_status(value: str | None) -> IncidentEventServiceStatus | None:
    if value is None:
        return None
    if value in INCIDENT_EVENT_SERVICE_STATUS_VALUES:
        return cast(IncidentEventServiceStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_EVENT_SERVICE_STATUS_VALUES!r}")
