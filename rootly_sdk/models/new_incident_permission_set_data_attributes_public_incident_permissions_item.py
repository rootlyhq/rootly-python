from typing import Literal, cast

NewIncidentPermissionSetDataAttributesPublicIncidentPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_INCIDENT_PERMISSION_SET_DATA_ATTRIBUTES_PUBLIC_INCIDENT_PERMISSIONS_ITEM_VALUES: set[
    NewIncidentPermissionSetDataAttributesPublicIncidentPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_incident_permission_set_data_attributes_public_incident_permissions_item(
    value: str | None,
) -> NewIncidentPermissionSetDataAttributesPublicIncidentPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_PERMISSION_SET_DATA_ATTRIBUTES_PUBLIC_INCIDENT_PERMISSIONS_ITEM_VALUES:
        return cast(NewIncidentPermissionSetDataAttributesPublicIncidentPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_PERMISSION_SET_DATA_ATTRIBUTES_PUBLIC_INCIDENT_PERMISSIONS_ITEM_VALUES!r}"
    )
