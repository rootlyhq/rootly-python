from typing import Literal, cast

RoleApiKeysPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_API_KEYS_PERMISSIONS_ITEM_VALUES: set[RoleApiKeysPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_api_keys_permissions_item(value: str | None) -> RoleApiKeysPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_API_KEYS_PERMISSIONS_ITEM_VALUES:
        return cast(RoleApiKeysPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_API_KEYS_PERMISSIONS_ITEM_VALUES!r}")
