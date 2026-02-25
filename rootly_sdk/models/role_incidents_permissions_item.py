from typing import Literal, cast

RoleIncidentsPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_INCIDENTS_PERMISSIONS_ITEM_VALUES: set[RoleIncidentsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_incidents_permissions_item(value: str | None) -> RoleIncidentsPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_INCIDENTS_PERMISSIONS_ITEM_VALUES:
        return cast(RoleIncidentsPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_INCIDENTS_PERMISSIONS_ITEM_VALUES!r}")
