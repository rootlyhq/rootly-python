from typing import Literal, cast

IncidentPermissionSetBooleanListDataItemType = Literal["incident_permission_set_booleans"]

INCIDENT_PERMISSION_SET_BOOLEAN_LIST_DATA_ITEM_TYPE_VALUES: set[IncidentPermissionSetBooleanListDataItemType] = {
    "incident_permission_set_booleans",
}


def check_incident_permission_set_boolean_list_data_item_type(
    value: str | None,
) -> IncidentPermissionSetBooleanListDataItemType | None:
    if value is None:
        return None
    if value in INCIDENT_PERMISSION_SET_BOOLEAN_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(IncidentPermissionSetBooleanListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_PERMISSION_SET_BOOLEAN_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
