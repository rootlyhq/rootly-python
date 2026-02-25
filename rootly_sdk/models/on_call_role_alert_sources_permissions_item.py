from typing import Literal, cast

OnCallRoleAlertSourcesPermissionsItem = Literal["create", "delete", "read", "update"]

ON_CALL_ROLE_ALERT_SOURCES_PERMISSIONS_ITEM_VALUES: set[OnCallRoleAlertSourcesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_on_call_role_alert_sources_permissions_item(value: str | None) -> OnCallRoleAlertSourcesPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_ALERT_SOURCES_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleAlertSourcesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_ALERT_SOURCES_PERMISSIONS_ITEM_VALUES!r}"
    )
