from typing import Literal, cast

UpdateOnCallRoleDataAttributesLiveCallRoutingPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_LIVE_CALL_ROUTING_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesLiveCallRoutingPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_on_call_role_data_attributes_live_call_routing_permissions_item(
    value: str | None,
) -> UpdateOnCallRoleDataAttributesLiveCallRoutingPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_LIVE_CALL_ROUTING_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateOnCallRoleDataAttributesLiveCallRoutingPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_LIVE_CALL_ROUTING_PERMISSIONS_ITEM_VALUES!r}"
    )
