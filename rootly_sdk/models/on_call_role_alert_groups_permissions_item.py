from typing import Literal, cast

OnCallRoleAlertGroupsPermissionsItem = Literal["create", "delete", "read", "update"]

ON_CALL_ROLE_ALERT_GROUPS_PERMISSIONS_ITEM_VALUES: set[OnCallRoleAlertGroupsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_on_call_role_alert_groups_permissions_item(value: str) -> OnCallRoleAlertGroupsPermissionsItem:
    if value in ON_CALL_ROLE_ALERT_GROUPS_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleAlertGroupsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_ALERT_GROUPS_PERMISSIONS_ITEM_VALUES!r}"
    )
