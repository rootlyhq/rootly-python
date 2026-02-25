from typing import Literal, cast

IncidentPermissionSetListDataItemType = Literal["incident_permission_sets"]

INCIDENT_PERMISSION_SET_LIST_DATA_ITEM_TYPE_VALUES: set[IncidentPermissionSetListDataItemType] = {
    "incident_permission_sets",
}


def check_incident_permission_set_list_data_item_type(
    value: str | None,
) -> IncidentPermissionSetListDataItemType | None:
    if value is None:
        return None
    if value in INCIDENT_PERMISSION_SET_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(IncidentPermissionSetListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_PERMISSION_SET_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
