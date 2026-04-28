from typing import Literal, cast

RoleSubStatusesPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_SUB_STATUSES_PERMISSIONS_ITEM_VALUES: set[RoleSubStatusesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_sub_statuses_permissions_item(value: str | None) -> RoleSubStatusesPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_SUB_STATUSES_PERMISSIONS_ITEM_VALUES:
        return cast(RoleSubStatusesPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_SUB_STATUSES_PERMISSIONS_ITEM_VALUES!r}")
