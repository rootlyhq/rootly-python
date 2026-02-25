from typing import Literal, cast

RoleEnvironmentsPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_ENVIRONMENTS_PERMISSIONS_ITEM_VALUES: set[RoleEnvironmentsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_environments_permissions_item(value: str | None) -> RoleEnvironmentsPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_ENVIRONMENTS_PERMISSIONS_ITEM_VALUES:
        return cast(RoleEnvironmentsPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_ENVIRONMENTS_PERMISSIONS_ITEM_VALUES!r}")
