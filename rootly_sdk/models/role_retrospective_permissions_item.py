from typing import Literal, cast

RoleRetrospectivePermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_RETROSPECTIVE_PERMISSIONS_ITEM_VALUES: set[RoleRetrospectivePermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_retrospective_permissions_item(value: str | None) -> RoleRetrospectivePermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_RETROSPECTIVE_PERMISSIONS_ITEM_VALUES:
        return cast(RoleRetrospectivePermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_RETROSPECTIVE_PERMISSIONS_ITEM_VALUES!r}")
