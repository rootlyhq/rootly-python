from typing import Literal, cast

NewIncidentEventServiceDataType = Literal["incident_event_services"]

NEW_INCIDENT_EVENT_SERVICE_DATA_TYPE_VALUES: set[NewIncidentEventServiceDataType] = {
    "incident_event_services",
}


def check_new_incident_event_service_data_type(value: str | None) -> NewIncidentEventServiceDataType | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_EVENT_SERVICE_DATA_TYPE_VALUES:
        return cast(NewIncidentEventServiceDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_EVENT_SERVICE_DATA_TYPE_VALUES!r}")
