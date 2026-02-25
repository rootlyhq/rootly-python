from typing import Literal, cast

IncidentTypeListDataItemType = Literal["incident_types"]

INCIDENT_TYPE_LIST_DATA_ITEM_TYPE_VALUES: set[IncidentTypeListDataItemType] = {
    "incident_types",
}


def check_incident_type_list_data_item_type(value: str | None) -> IncidentTypeListDataItemType | None:
    if value is None:
        return None
    if value in INCIDENT_TYPE_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(IncidentTypeListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_TYPE_LIST_DATA_ITEM_TYPE_VALUES!r}")
