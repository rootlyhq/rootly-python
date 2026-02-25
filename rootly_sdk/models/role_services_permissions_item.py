from typing import Literal, cast

RoleServicesPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_SERVICES_PERMISSIONS_ITEM_VALUES: set[RoleServicesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_services_permissions_item(value: str | None) -> RoleServicesPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_SERVICES_PERMISSIONS_ITEM_VALUES:
        return cast(RoleServicesPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_SERVICES_PERMISSIONS_ITEM_VALUES!r}")
