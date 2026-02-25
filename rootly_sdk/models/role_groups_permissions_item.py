from typing import Literal, cast

RoleGroupsPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_GROUPS_PERMISSIONS_ITEM_VALUES: set[RoleGroupsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_groups_permissions_item(value: str | None) -> RoleGroupsPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_GROUPS_PERMISSIONS_ITEM_VALUES:
        return cast(RoleGroupsPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_GROUPS_PERMISSIONS_ITEM_VALUES!r}")
