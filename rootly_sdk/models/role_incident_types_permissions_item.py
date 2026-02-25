from typing import Literal, cast

RoleIncidentTypesPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_INCIDENT_TYPES_PERMISSIONS_ITEM_VALUES: set[RoleIncidentTypesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_incident_types_permissions_item(value: str | None) -> RoleIncidentTypesPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_INCIDENT_TYPES_PERMISSIONS_ITEM_VALUES:
        return cast(RoleIncidentTypesPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_INCIDENT_TYPES_PERMISSIONS_ITEM_VALUES!r}")
