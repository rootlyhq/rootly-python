from typing import Literal, cast

OnCallRoleAlertUrgencyPermissionsItem = Literal["create", "delete", "read", "update"]

ON_CALL_ROLE_ALERT_URGENCY_PERMISSIONS_ITEM_VALUES: set[OnCallRoleAlertUrgencyPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_on_call_role_alert_urgency_permissions_item(value: str | None) -> OnCallRoleAlertUrgencyPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_ALERT_URGENCY_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleAlertUrgencyPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_ALERT_URGENCY_PERMISSIONS_ITEM_VALUES!r}"
    )
