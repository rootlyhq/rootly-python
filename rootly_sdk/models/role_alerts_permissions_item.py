from typing import Literal, cast

RoleAlertsPermissionsItem = Literal["create", "read"]

ROLE_ALERTS_PERMISSIONS_ITEM_VALUES: set[RoleAlertsPermissionsItem] = {
    "create",
    "read",
}


def check_role_alerts_permissions_item(value: str | None) -> RoleAlertsPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_ALERTS_PERMISSIONS_ITEM_VALUES:
        return cast(RoleAlertsPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_ALERTS_PERMISSIONS_ITEM_VALUES!r}")
