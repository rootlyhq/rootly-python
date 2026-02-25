from typing import Literal, cast

NewIncidentStatusPageEventDataType = Literal["incident_status_page_events"]

NEW_INCIDENT_STATUS_PAGE_EVENT_DATA_TYPE_VALUES: set[NewIncidentStatusPageEventDataType] = {
    "incident_status_page_events",
}


def check_new_incident_status_page_event_data_type(value: str | None) -> NewIncidentStatusPageEventDataType | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_STATUS_PAGE_EVENT_DATA_TYPE_VALUES:
        return cast(NewIncidentStatusPageEventDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_STATUS_PAGE_EVENT_DATA_TYPE_VALUES!r}")
