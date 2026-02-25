from typing import Literal, cast

RoleSeveritiesPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_SEVERITIES_PERMISSIONS_ITEM_VALUES: set[RoleSeveritiesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_severities_permissions_item(value: str | None) -> RoleSeveritiesPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_SEVERITIES_PERMISSIONS_ITEM_VALUES:
        return cast(RoleSeveritiesPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_SEVERITIES_PERMISSIONS_ITEM_VALUES!r}")
