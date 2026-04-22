from typing import Literal, cast

RolePagingPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_PAGING_PERMISSIONS_ITEM_VALUES: set[RolePagingPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_paging_permissions_item(value: str | None) -> RolePagingPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_PAGING_PERMISSIONS_ITEM_VALUES:
        return cast(RolePagingPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_PAGING_PERMISSIONS_ITEM_VALUES!r}")
