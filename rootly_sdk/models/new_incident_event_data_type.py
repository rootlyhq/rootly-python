from typing import Literal, cast

NewIncidentEventDataType = Literal["incident_events"]

NEW_INCIDENT_EVENT_DATA_TYPE_VALUES: set[NewIncidentEventDataType] = {
    "incident_events",
}


def check_new_incident_event_data_type(value: str | None) -> NewIncidentEventDataType | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_EVENT_DATA_TYPE_VALUES:
        return cast(NewIncidentEventDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_EVENT_DATA_TYPE_VALUES!r}")
