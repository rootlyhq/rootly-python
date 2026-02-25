from typing import Literal, cast

RoleIncidentRolesPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_INCIDENT_ROLES_PERMISSIONS_ITEM_VALUES: set[RoleIncidentRolesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_incident_roles_permissions_item(value: str | None) -> RoleIncidentRolesPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_INCIDENT_ROLES_PERMISSIONS_ITEM_VALUES:
        return cast(RoleIncidentRolesPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_INCIDENT_ROLES_PERMISSIONS_ITEM_VALUES!r}")
