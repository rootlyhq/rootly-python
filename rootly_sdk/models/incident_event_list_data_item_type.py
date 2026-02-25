from typing import Literal, cast

IncidentEventListDataItemType = Literal["incident_events"]

INCIDENT_EVENT_LIST_DATA_ITEM_TYPE_VALUES: set[IncidentEventListDataItemType] = {
    "incident_events",
}


def check_incident_event_list_data_item_type(value: str | None) -> IncidentEventListDataItemType | None:
    if value is None:
        return None
    if value in INCIDENT_EVENT_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(IncidentEventListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_EVENT_LIST_DATA_ITEM_TYPE_VALUES!r}")
