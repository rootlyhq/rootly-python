from typing import Literal, cast

IncidentPermissionSetResourceListDataItemType = Literal["incident_permission_set_resources"]

INCIDENT_PERMISSION_SET_RESOURCE_LIST_DATA_ITEM_TYPE_VALUES: set[IncidentPermissionSetResourceListDataItemType] = {
    "incident_permission_set_resources",
}


def check_incident_permission_set_resource_list_data_item_type(
    value: str | None,
) -> IncidentPermissionSetResourceListDataItemType | None:
    if value is None:
        return None
    if value in INCIDENT_PERMISSION_SET_RESOURCE_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(IncidentPermissionSetResourceListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_PERMISSION_SET_RESOURCE_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
