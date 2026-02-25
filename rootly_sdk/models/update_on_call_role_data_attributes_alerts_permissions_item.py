from typing import Literal, cast

UpdateOnCallRoleDataAttributesAlertsPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERTS_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesAlertsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_on_call_role_data_attributes_alerts_permissions_item(
    value: str | None,
) -> UpdateOnCallRoleDataAttributesAlertsPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERTS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateOnCallRoleDataAttributesAlertsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERTS_PERMISSIONS_ITEM_VALUES!r}"
    )
