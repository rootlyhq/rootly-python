from typing import Literal, cast

UpdateOnCallRoleDataAttributesHeartbeatsPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_HEARTBEATS_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesHeartbeatsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_on_call_role_data_attributes_heartbeats_permissions_item(
    value: str | None,
) -> UpdateOnCallRoleDataAttributesHeartbeatsPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_HEARTBEATS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateOnCallRoleDataAttributesHeartbeatsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_HEARTBEATS_PERMISSIONS_ITEM_VALUES!r}"
    )
