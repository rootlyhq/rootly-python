from typing import Literal, cast

RoleAuditsPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_AUDITS_PERMISSIONS_ITEM_VALUES: set[RoleAuditsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_audits_permissions_item(value: str | None) -> RoleAuditsPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_AUDITS_PERMISSIONS_ITEM_VALUES:
        return cast(RoleAuditsPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_AUDITS_PERMISSIONS_ITEM_VALUES!r}")
