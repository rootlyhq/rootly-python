from typing import Literal, cast

IncidentSubStatusListDataItemType = Literal["incident_sub_statuses"]

INCIDENT_SUB_STATUS_LIST_DATA_ITEM_TYPE_VALUES: set[IncidentSubStatusListDataItemType] = {
    "incident_sub_statuses",
}


def check_incident_sub_status_list_data_item_type(value: str | None) -> IncidentSubStatusListDataItemType | None:
    if value is None:
        return None
    if value in INCIDENT_SUB_STATUS_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(IncidentSubStatusListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_SUB_STATUS_LIST_DATA_ITEM_TYPE_VALUES!r}")
