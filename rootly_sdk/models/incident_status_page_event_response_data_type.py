from typing import Literal, cast

IncidentStatusPageEventResponseDataType = Literal["incident_status_page_events"]

INCIDENT_STATUS_PAGE_EVENT_RESPONSE_DATA_TYPE_VALUES: set[IncidentStatusPageEventResponseDataType] = {
    "incident_status_page_events",
}


def check_incident_status_page_event_response_data_type(value: str | None) -> IncidentStatusPageEventResponseDataType | None:
    if value is None:
        return None
    if value in INCIDENT_STATUS_PAGE_EVENT_RESPONSE_DATA_TYPE_VALUES:
        return cast(IncidentStatusPageEventResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_STATUS_PAGE_EVENT_RESPONSE_DATA_TYPE_VALUES!r}"
    )
