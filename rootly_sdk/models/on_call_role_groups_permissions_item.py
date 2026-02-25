from typing import Literal, cast

OnCallRoleGroupsPermissionsItem = Literal["create", "delete", "read", "update"]

ON_CALL_ROLE_GROUPS_PERMISSIONS_ITEM_VALUES: set[OnCallRoleGroupsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_on_call_role_groups_permissions_item(value: str | None) -> OnCallRoleGroupsPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_GROUPS_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleGroupsPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_GROUPS_PERMISSIONS_ITEM_VALUES!r}")
