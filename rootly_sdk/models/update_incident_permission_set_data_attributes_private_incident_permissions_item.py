from typing import Literal, cast

UpdateIncidentPermissionSetDataAttributesPrivateIncidentPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_INCIDENT_PERMISSION_SET_DATA_ATTRIBUTES_PRIVATE_INCIDENT_PERMISSIONS_ITEM_VALUES: set[
    UpdateIncidentPermissionSetDataAttributesPrivateIncidentPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_incident_permission_set_data_attributes_private_incident_permissions_item(
    value: str | None,
) -> UpdateIncidentPermissionSetDataAttributesPrivateIncidentPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_PERMISSION_SET_DATA_ATTRIBUTES_PRIVATE_INCIDENT_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateIncidentPermissionSetDataAttributesPrivateIncidentPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_PERMISSION_SET_DATA_ATTRIBUTES_PRIVATE_INCIDENT_PERMISSIONS_ITEM_VALUES!r}"
    )
