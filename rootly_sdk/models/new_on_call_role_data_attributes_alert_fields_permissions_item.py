from typing import Literal, cast

NewOnCallRoleDataAttributesAlertFieldsPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_FIELDS_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesAlertFieldsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_on_call_role_data_attributes_alert_fields_permissions_item(
    value: str,
) -> NewOnCallRoleDataAttributesAlertFieldsPermissionsItem:
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_FIELDS_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesAlertFieldsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_FIELDS_PERMISSIONS_ITEM_VALUES!r}"
    )
