from typing import Literal, cast

UpdateIncidentStatusPageEventDataType = Literal["incident_status_page_events"]

UPDATE_INCIDENT_STATUS_PAGE_EVENT_DATA_TYPE_VALUES: set[UpdateIncidentStatusPageEventDataType] = {
    "incident_status_page_events",
}


def check_update_incident_status_page_event_data_type(value: str | None) -> UpdateIncidentStatusPageEventDataType | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_STATUS_PAGE_EVENT_DATA_TYPE_VALUES:
        return cast(UpdateIncidentStatusPageEventDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_STATUS_PAGE_EVENT_DATA_TYPE_VALUES!r}"
    )
