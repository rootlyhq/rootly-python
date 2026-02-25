from typing import Literal, cast

IncidentEventServiceResponseDataType = Literal["incident_event_services"]

INCIDENT_EVENT_SERVICE_RESPONSE_DATA_TYPE_VALUES: set[IncidentEventServiceResponseDataType] = {
    "incident_event_services",
}


def check_incident_event_service_response_data_type(value: str | None) -> IncidentEventServiceResponseDataType | None:
    if value is None:
        return None
    if value in INCIDENT_EVENT_SERVICE_RESPONSE_DATA_TYPE_VALUES:
        return cast(IncidentEventServiceResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_EVENT_SERVICE_RESPONSE_DATA_TYPE_VALUES!r}")
