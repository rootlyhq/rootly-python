from typing import Literal, cast

IncidentRoleListDataItemType = Literal["incident_roles"]

INCIDENT_ROLE_LIST_DATA_ITEM_TYPE_VALUES: set[IncidentRoleListDataItemType] = {
    "incident_roles",
}


def check_incident_role_list_data_item_type(value: str | None) -> IncidentRoleListDataItemType | None:
    if value is None:
        return None
    if value in INCIDENT_ROLE_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(IncidentRoleListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_ROLE_LIST_DATA_ITEM_TYPE_VALUES!r}")
