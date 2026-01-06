from typing import Literal, cast

NewOnCallRoleDataAttributesAlertGroupsPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_GROUPS_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesAlertGroupsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_on_call_role_data_attributes_alert_groups_permissions_item(
    value: str,
) -> NewOnCallRoleDataAttributesAlertGroupsPermissionsItem:
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_GROUPS_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesAlertGroupsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_GROUPS_PERMISSIONS_ITEM_VALUES!r}"
    )
