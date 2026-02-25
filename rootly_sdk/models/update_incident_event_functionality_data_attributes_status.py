from typing import Literal, cast

UpdateIncidentEventFunctionalityDataAttributesStatus = Literal["major_outage", "operational", "partial_outage"]

UPDATE_INCIDENT_EVENT_FUNCTIONALITY_DATA_ATTRIBUTES_STATUS_VALUES: set[
    UpdateIncidentEventFunctionalityDataAttributesStatus
] = {
    "major_outage",
    "operational",
    "partial_outage",
}


def check_update_incident_event_functionality_data_attributes_status(
    value: str | None,
) -> UpdateIncidentEventFunctionalityDataAttributesStatus | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_EVENT_FUNCTIONALITY_DATA_ATTRIBUTES_STATUS_VALUES:
        return cast(UpdateIncidentEventFunctionalityDataAttributesStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_EVENT_FUNCTIONALITY_DATA_ATTRIBUTES_STATUS_VALUES!r}"
    )
