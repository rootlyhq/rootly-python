from typing import Literal

UpdateIncidentEventDataAttributesVisibility = Literal["external", "internal"]

UPDATE_INCIDENT_EVENT_DATA_ATTRIBUTES_VISIBILITY_VALUES: set[UpdateIncidentEventDataAttributesVisibility] = {
    "external",
    "internal",
}


def check_update_incident_event_data_attributes_visibility(
    value: str | None,
) -> UpdateIncidentEventDataAttributesVisibility | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_EVENT_DATA_ATTRIBUTES_VISIBILITY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_EVENT_DATA_ATTRIBUTES_VISIBILITY_VALUES!r}"
    )
