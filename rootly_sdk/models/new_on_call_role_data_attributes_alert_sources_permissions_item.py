from typing import Literal, cast

NewOnCallRoleDataAttributesAlertSourcesPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_SOURCES_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesAlertSourcesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_on_call_role_data_attributes_alert_sources_permissions_item(
    value: str | None,
) -> NewOnCallRoleDataAttributesAlertSourcesPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_SOURCES_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesAlertSourcesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_SOURCES_PERMISSIONS_ITEM_VALUES!r}"
    )
