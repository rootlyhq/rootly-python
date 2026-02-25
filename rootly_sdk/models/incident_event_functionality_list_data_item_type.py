from typing import Literal, cast

IncidentEventFunctionalityListDataItemType = Literal["incident_event_functionalities"]

INCIDENT_EVENT_FUNCTIONALITY_LIST_DATA_ITEM_TYPE_VALUES: set[IncidentEventFunctionalityListDataItemType] = {
    "incident_event_functionalities",
}


def check_incident_event_functionality_list_data_item_type(value: str | None) -> IncidentEventFunctionalityListDataItemType | None:
    if value is None:
        return None
    if value in INCIDENT_EVENT_FUNCTIONALITY_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(IncidentEventFunctionalityListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_EVENT_FUNCTIONALITY_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
