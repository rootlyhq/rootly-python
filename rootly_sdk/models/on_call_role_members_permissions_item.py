from typing import Literal

OnCallRoleMembersPermissionsItem = Literal["delete", "read", "update"]

ON_CALL_ROLE_MEMBERS_PERMISSIONS_ITEM_VALUES: set[OnCallRoleMembersPermissionsItem] = {
    "delete",
    "read",
    "update",
}


def check_on_call_role_members_permissions_item(value: str | None) -> OnCallRoleMembersPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_MEMBERS_PERMISSIONS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_MEMBERS_PERMISSIONS_ITEM_VALUES!r}")
