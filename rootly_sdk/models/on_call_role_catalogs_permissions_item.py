from typing import Literal, cast

OnCallRoleCatalogsPermissionsItem = Literal["create", "delete", "read", "update"]

ON_CALL_ROLE_CATALOGS_PERMISSIONS_ITEM_VALUES: set[OnCallRoleCatalogsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_on_call_role_catalogs_permissions_item(value: str | None) -> OnCallRoleCatalogsPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_CATALOGS_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleCatalogsPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_CATALOGS_PERMISSIONS_ITEM_VALUES!r}")
