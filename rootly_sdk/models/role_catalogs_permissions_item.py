from typing import Literal, cast

RoleCatalogsPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_CATALOGS_PERMISSIONS_ITEM_VALUES: set[RoleCatalogsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_catalogs_permissions_item(value: str | None) -> RoleCatalogsPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_CATALOGS_PERMISSIONS_ITEM_VALUES:
        return cast(RoleCatalogsPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_CATALOGS_PERMISSIONS_ITEM_VALUES!r}")
