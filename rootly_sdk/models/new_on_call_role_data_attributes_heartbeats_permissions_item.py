from typing import Literal, cast

NewOnCallRoleDataAttributesHeartbeatsPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_HEARTBEATS_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesHeartbeatsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_on_call_role_data_attributes_heartbeats_permissions_item(
    value: str | None,
) -> NewOnCallRoleDataAttributesHeartbeatsPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_HEARTBEATS_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesHeartbeatsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_HEARTBEATS_PERMISSIONS_ITEM_VALUES!r}"
    )
