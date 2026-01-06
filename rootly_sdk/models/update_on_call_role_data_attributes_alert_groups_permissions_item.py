from typing import Literal, cast

UpdateOnCallRoleDataAttributesAlertGroupsPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_GROUPS_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesAlertGroupsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_on_call_role_data_attributes_alert_groups_permissions_item(
    value: str,
) -> UpdateOnCallRoleDataAttributesAlertGroupsPermissionsItem:
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_GROUPS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateOnCallRoleDataAttributesAlertGroupsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_GROUPS_PERMISSIONS_ITEM_VALUES!r}"
    )
