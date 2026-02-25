from typing import Literal, cast

IncidentPermissionSetPrivateIncidentPermissionsItem = Literal["create", "delete", "read", "update"]

INCIDENT_PERMISSION_SET_PRIVATE_INCIDENT_PERMISSIONS_ITEM_VALUES: set[
    IncidentPermissionSetPrivateIncidentPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_incident_permission_set_private_incident_permissions_item(
    value: str | None,
) -> IncidentPermissionSetPrivateIncidentPermissionsItem | None:
    if value is None:
        return None
    if value in INCIDENT_PERMISSION_SET_PRIVATE_INCIDENT_PERMISSIONS_ITEM_VALUES:
        return cast(IncidentPermissionSetPrivateIncidentPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_PERMISSION_SET_PRIVATE_INCIDENT_PERMISSIONS_ITEM_VALUES!r}"
    )
