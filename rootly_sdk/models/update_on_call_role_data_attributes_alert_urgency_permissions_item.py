from typing import Literal, cast

UpdateOnCallRoleDataAttributesAlertUrgencyPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_URGENCY_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesAlertUrgencyPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_on_call_role_data_attributes_alert_urgency_permissions_item(
    value: str | None,
) -> UpdateOnCallRoleDataAttributesAlertUrgencyPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_URGENCY_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateOnCallRoleDataAttributesAlertUrgencyPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_URGENCY_PERMISSIONS_ITEM_VALUES!r}"
    )
