from typing import Literal

RoleSlasPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_SLAS_PERMISSIONS_ITEM_VALUES: set[RoleSlasPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_slas_permissions_item(value: str | None) -> RoleSlasPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_SLAS_PERMISSIONS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_SLAS_PERMISSIONS_ITEM_VALUES!r}")
