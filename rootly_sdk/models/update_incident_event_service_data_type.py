from typing import Literal, cast

UpdateIncidentEventServiceDataType = Literal["incident_event_services"]

UPDATE_INCIDENT_EVENT_SERVICE_DATA_TYPE_VALUES: set[UpdateIncidentEventServiceDataType] = {
    "incident_event_services",
}


def check_update_incident_event_service_data_type(value: str | None) -> UpdateIncidentEventServiceDataType | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_EVENT_SERVICE_DATA_TYPE_VALUES:
        return cast(UpdateIncidentEventServiceDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_EVENT_SERVICE_DATA_TYPE_VALUES!r}")
