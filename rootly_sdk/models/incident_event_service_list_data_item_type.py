from typing import Literal, cast

IncidentEventServiceListDataItemType = Literal["incident_event_services"]

INCIDENT_EVENT_SERVICE_LIST_DATA_ITEM_TYPE_VALUES: set[IncidentEventServiceListDataItemType] = {
    "incident_event_services",
}


def check_incident_event_service_list_data_item_type(value: str | None) -> IncidentEventServiceListDataItemType | None:
    if value is None:
        return None
    if value in INCIDENT_EVENT_SERVICE_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(IncidentEventServiceListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_EVENT_SERVICE_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
