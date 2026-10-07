from typing import Literal

AuthorizationPermissionsItem = Literal["authorize", "destroy", "read", "update"]

AUTHORIZATION_PERMISSIONS_ITEM_VALUES: set[AuthorizationPermissionsItem] = {
    "authorize",
    "destroy",
    "read",
    "update",
}


def check_authorization_permissions_item(value: str | None) -> AuthorizationPermissionsItem | None:
    if value is None:
        return None
    if value in AUTHORIZATION_PERMISSIONS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AUTHORIZATION_PERMISSIONS_ITEM_VALUES!r}")
