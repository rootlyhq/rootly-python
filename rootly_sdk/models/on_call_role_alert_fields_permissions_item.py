from typing import Literal, cast

OnCallRoleAlertFieldsPermissionsItem = Literal["create", "delete", "read", "update"]

ON_CALL_ROLE_ALERT_FIELDS_PERMISSIONS_ITEM_VALUES: set[OnCallRoleAlertFieldsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_on_call_role_alert_fields_permissions_item(value: str | None) -> OnCallRoleAlertFieldsPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_ALERT_FIELDS_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleAlertFieldsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_ALERT_FIELDS_PERMISSIONS_ITEM_VALUES!r}"
    )
