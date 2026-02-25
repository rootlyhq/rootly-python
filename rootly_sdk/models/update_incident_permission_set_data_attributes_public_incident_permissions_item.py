from typing import Literal, cast

UpdateIncidentPermissionSetDataAttributesPublicIncidentPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_INCIDENT_PERMISSION_SET_DATA_ATTRIBUTES_PUBLIC_INCIDENT_PERMISSIONS_ITEM_VALUES: set[
    UpdateIncidentPermissionSetDataAttributesPublicIncidentPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_incident_permission_set_data_attributes_public_incident_permissions_item(
    value: str | None,
) -> UpdateIncidentPermissionSetDataAttributesPublicIncidentPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_PERMISSION_SET_DATA_ATTRIBUTES_PUBLIC_INCIDENT_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateIncidentPermissionSetDataAttributesPublicIncidentPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_PERMISSION_SET_DATA_ATTRIBUTES_PUBLIC_INCIDENT_PERMISSIONS_ITEM_VALUES!r}"
    )
