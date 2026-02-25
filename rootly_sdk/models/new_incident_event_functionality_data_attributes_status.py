from typing import Literal, cast

NewIncidentEventFunctionalityDataAttributesStatus = Literal["major_outage", "operational", "partial_outage"]

NEW_INCIDENT_EVENT_FUNCTIONALITY_DATA_ATTRIBUTES_STATUS_VALUES: set[
    NewIncidentEventFunctionalityDataAttributesStatus
] = {
    "major_outage",
    "operational",
    "partial_outage",
}


def check_new_incident_event_functionality_data_attributes_status(
    value: str | None,
) -> NewIncidentEventFunctionalityDataAttributesStatus | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_EVENT_FUNCTIONALITY_DATA_ATTRIBUTES_STATUS_VALUES:
        return cast(NewIncidentEventFunctionalityDataAttributesStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_EVENT_FUNCTIONALITY_DATA_ATTRIBUTES_STATUS_VALUES!r}"
    )
