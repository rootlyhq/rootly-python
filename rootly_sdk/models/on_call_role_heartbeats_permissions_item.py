from typing import Literal, cast

OnCallRoleHeartbeatsPermissionsItem = Literal["create", "delete", "read", "update"]

ON_CALL_ROLE_HEARTBEATS_PERMISSIONS_ITEM_VALUES: set[OnCallRoleHeartbeatsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_on_call_role_heartbeats_permissions_item(value: str | None) -> OnCallRoleHeartbeatsPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_HEARTBEATS_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleHeartbeatsPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_HEARTBEATS_PERMISSIONS_ITEM_VALUES!r}")
