from typing import Literal, cast

OnCallRoleOnCallRolesPermissionsItem = Literal["create", "delete", "read", "update"]

ON_CALL_ROLE_ON_CALL_ROLES_PERMISSIONS_ITEM_VALUES: set[OnCallRoleOnCallRolesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_on_call_role_on_call_roles_permissions_item(value: str | None) -> OnCallRoleOnCallRolesPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_ON_CALL_ROLES_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleOnCallRolesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_ON_CALL_ROLES_PERMISSIONS_ITEM_VALUES!r}"
    )
