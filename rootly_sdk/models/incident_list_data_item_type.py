from typing import Literal, cast

IncidentListDataItemType = Literal["incidents"]

INCIDENT_LIST_DATA_ITEM_TYPE_VALUES: set[IncidentListDataItemType] = {
    "incidents",
}


def check_incident_list_data_item_type(value: str | None) -> IncidentListDataItemType | None:
    if value is None:
        return None
    if value in INCIDENT_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(IncidentListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_LIST_DATA_ITEM_TYPE_VALUES!r}")
