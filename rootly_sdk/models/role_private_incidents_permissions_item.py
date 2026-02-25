from typing import Literal, cast

RolePrivateIncidentsPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_PRIVATE_INCIDENTS_PERMISSIONS_ITEM_VALUES: set[RolePrivateIncidentsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_private_incidents_permissions_item(value: str | None) -> RolePrivateIncidentsPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_PRIVATE_INCIDENTS_PERMISSIONS_ITEM_VALUES:
        return cast(RolePrivateIncidentsPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_PRIVATE_INCIDENTS_PERMISSIONS_ITEM_VALUES!r}")
