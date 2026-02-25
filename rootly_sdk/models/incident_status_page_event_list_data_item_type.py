from typing import Literal, cast

IncidentStatusPageEventListDataItemType = Literal["incident_status_page_events"]

INCIDENT_STATUS_PAGE_EVENT_LIST_DATA_ITEM_TYPE_VALUES: set[IncidentStatusPageEventListDataItemType] = {
    "incident_status_page_events",
}


def check_incident_status_page_event_list_data_item_type(
    value: str | None,
) -> IncidentStatusPageEventListDataItemType | None:
    if value is None:
        return None
    if value in INCIDENT_STATUS_PAGE_EVENT_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(IncidentStatusPageEventListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_STATUS_PAGE_EVENT_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
