from typing import Literal, cast

RoleRolesPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_ROLES_PERMISSIONS_ITEM_VALUES: set[RoleRolesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_roles_permissions_item(value: str | None) -> RoleRolesPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_ROLES_PERMISSIONS_ITEM_VALUES:
        return cast(RoleRolesPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_ROLES_PERMISSIONS_ITEM_VALUES!r}")
