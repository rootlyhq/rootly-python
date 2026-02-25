from typing import Literal, cast

NewOnCallRoleDataAttributesAlertUrgencyPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_URGENCY_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesAlertUrgencyPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_on_call_role_data_attributes_alert_urgency_permissions_item(
    value: str | None,
) -> NewOnCallRoleDataAttributesAlertUrgencyPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_URGENCY_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesAlertUrgencyPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_URGENCY_PERMISSIONS_ITEM_VALUES!r}"
    )
