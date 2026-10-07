from typing import Literal

IncidentEventResponseDataType = Literal["incident_events"]

INCIDENT_EVENT_RESPONSE_DATA_TYPE_VALUES: set[IncidentEventResponseDataType] = {
    "incident_events",
}


def check_incident_event_response_data_type(value: str | None) -> IncidentEventResponseDataType | None:
    if value is None:
        return None
    if value in INCIDENT_EVENT_RESPONSE_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_EVENT_RESPONSE_DATA_TYPE_VALUES!r}")
