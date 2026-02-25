from typing import Literal, cast

IncidentPermissionSetPublicIncidentPermissionsItem = Literal["create", "delete", "read", "update"]

INCIDENT_PERMISSION_SET_PUBLIC_INCIDENT_PERMISSIONS_ITEM_VALUES: set[
    IncidentPermissionSetPublicIncidentPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_incident_permission_set_public_incident_permissions_item(
    value: str | None,
) -> IncidentPermissionSetPublicIncidentPermissionsItem | None:
    if value is None:
        return None
    if value in INCIDENT_PERMISSION_SET_PUBLIC_INCIDENT_PERMISSIONS_ITEM_VALUES:
        return cast(IncidentPermissionSetPublicIncidentPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_PERMISSION_SET_PUBLIC_INCIDENT_PERMISSIONS_ITEM_VALUES!r}"
    )
