from typing import Literal

NewIncidentEventDataAttributesVisibility = Literal["external", "internal"]

NEW_INCIDENT_EVENT_DATA_ATTRIBUTES_VISIBILITY_VALUES: set[NewIncidentEventDataAttributesVisibility] = {
    "external",
    "internal",
}


def check_new_incident_event_data_attributes_visibility(
    value: str | None,
) -> NewIncidentEventDataAttributesVisibility | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_EVENT_DATA_ATTRIBUTES_VISIBILITY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_EVENT_DATA_ATTRIBUTES_VISIBILITY_VALUES!r}"
    )
