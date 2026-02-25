from typing import Literal, cast

NewIncidentPermissionSetDataAttributesPrivateIncidentPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_INCIDENT_PERMISSION_SET_DATA_ATTRIBUTES_PRIVATE_INCIDENT_PERMISSIONS_ITEM_VALUES: set[
    NewIncidentPermissionSetDataAttributesPrivateIncidentPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_incident_permission_set_data_attributes_private_incident_permissions_item(
    value: str | None,
) -> NewIncidentPermissionSetDataAttributesPrivateIncidentPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_PERMISSION_SET_DATA_ATTRIBUTES_PRIVATE_INCIDENT_PERMISSIONS_ITEM_VALUES:
        return cast(NewIncidentPermissionSetDataAttributesPrivateIncidentPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_PERMISSION_SET_DATA_ATTRIBUTES_PRIVATE_INCIDENT_PERMISSIONS_ITEM_VALUES!r}"
    )
