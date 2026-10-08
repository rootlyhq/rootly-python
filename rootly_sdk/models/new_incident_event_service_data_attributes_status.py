from typing import Literal

NewIncidentEventServiceDataAttributesStatus = Literal["major_outage", "operational", "partial_outage"]

NEW_INCIDENT_EVENT_SERVICE_DATA_ATTRIBUTES_STATUS_VALUES: set[NewIncidentEventServiceDataAttributesStatus] = {
    "major_outage",
    "operational",
    "partial_outage",
}


def check_new_incident_event_service_data_attributes_status(
    value: str | None,
) -> NewIncidentEventServiceDataAttributesStatus | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_EVENT_SERVICE_DATA_ATTRIBUTES_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_EVENT_SERVICE_DATA_ATTRIBUTES_STATUS_VALUES!r}"
    )
