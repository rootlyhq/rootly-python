from typing import Literal, cast

OnCallRoleApiKeysPermissionsItem = Literal["create", "delete", "read", "update"]

ON_CALL_ROLE_API_KEYS_PERMISSIONS_ITEM_VALUES: set[OnCallRoleApiKeysPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_on_call_role_api_keys_permissions_item(value: str | None) -> OnCallRoleApiKeysPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_API_KEYS_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleApiKeysPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_API_KEYS_PERMISSIONS_ITEM_VALUES!r}")
