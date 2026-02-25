from typing import Literal, cast

RoleStatusPagesPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_STATUS_PAGES_PERMISSIONS_ITEM_VALUES: set[RoleStatusPagesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_status_pages_permissions_item(value: str | None) -> RoleStatusPagesPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_STATUS_PAGES_PERMISSIONS_ITEM_VALUES:
        return cast(RoleStatusPagesPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_STATUS_PAGES_PERMISSIONS_ITEM_VALUES!r}")
