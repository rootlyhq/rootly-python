from typing import Literal, cast

UpdateIncidentStatusPageEventDataAttributesStatus = Literal[
    "completed", "identified", "in_progress", "investigating", "monitoring", "resolved", "scheduled"
]

UPDATE_INCIDENT_STATUS_PAGE_EVENT_DATA_ATTRIBUTES_STATUS_VALUES: set[
    UpdateIncidentStatusPageEventDataAttributesStatus
] = {
    "completed",
    "identified",
    "in_progress",
    "investigating",
    "monitoring",
    "resolved",
    "scheduled",
}


def check_update_incident_status_page_event_data_attributes_status(
    value: str | None,
) -> UpdateIncidentStatusPageEventDataAttributesStatus | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_STATUS_PAGE_EVENT_DATA_ATTRIBUTES_STATUS_VALUES:
        return cast(UpdateIncidentStatusPageEventDataAttributesStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_STATUS_PAGE_EVENT_DATA_ATTRIBUTES_STATUS_VALUES!r}"
    )
