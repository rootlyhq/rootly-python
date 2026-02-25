from typing import Literal, cast

NewIncidentStatusPageEventDataAttributesStatus = Literal[
    "completed", "identified", "in_progress", "investigating", "monitoring", "resolved", "scheduled"
]

NEW_INCIDENT_STATUS_PAGE_EVENT_DATA_ATTRIBUTES_STATUS_VALUES: set[NewIncidentStatusPageEventDataAttributesStatus] = {
    "completed",
    "identified",
    "in_progress",
    "investigating",
    "monitoring",
    "resolved",
    "scheduled",
}


def check_new_incident_status_page_event_data_attributes_status(
    value: str | None,
) -> NewIncidentStatusPageEventDataAttributesStatus | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_STATUS_PAGE_EVENT_DATA_ATTRIBUTES_STATUS_VALUES:
        return cast(NewIncidentStatusPageEventDataAttributesStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_STATUS_PAGE_EVENT_DATA_ATTRIBUTES_STATUS_VALUES!r}"
    )
