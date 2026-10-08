from typing import Literal

UpdateIncidentEventDataType = Literal["incident_events"]

UPDATE_INCIDENT_EVENT_DATA_TYPE_VALUES: set[UpdateIncidentEventDataType] = {
    "incident_events",
}


def check_update_incident_event_data_type(value: str | None) -> UpdateIncidentEventDataType | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_EVENT_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_EVENT_DATA_TYPE_VALUES!r}")
