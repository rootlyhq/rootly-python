from typing import Literal, cast

OnCallRoleAlertsPermissionsItem = Literal["create", "delete", "read", "update"]

ON_CALL_ROLE_ALERTS_PERMISSIONS_ITEM_VALUES: set[OnCallRoleAlertsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_on_call_role_alerts_permissions_item(value: str | None) -> OnCallRoleAlertsPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_ALERTS_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleAlertsPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_ALERTS_PERMISSIONS_ITEM_VALUES!r}")
