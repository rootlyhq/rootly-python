from typing import Literal, cast

UpdateOnCallRoleDataAttributesAlertFieldsPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_FIELDS_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesAlertFieldsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_on_call_role_data_attributes_alert_fields_permissions_item(
    value: str,
) -> UpdateOnCallRoleDataAttributesAlertFieldsPermissionsItem:
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_FIELDS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateOnCallRoleDataAttributesAlertFieldsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_FIELDS_PERMISSIONS_ITEM_VALUES!r}"
    )
