from typing import Literal, cast

IncidentEventVisibility = Literal["external", "internal"]

INCIDENT_EVENT_VISIBILITY_VALUES: set[IncidentEventVisibility] = {
    "external",
    "internal",
}


def check_incident_event_visibility(value: str | None) -> IncidentEventVisibility | None:
    if value is None:
        return None
    if value in INCIDENT_EVENT_VISIBILITY_VALUES:
        return cast(IncidentEventVisibility, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_EVENT_VISIBILITY_VALUES!r}")
