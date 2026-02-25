from typing import Literal, cast

NewOnCallRoleDataAttributesLiveCallRoutingPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_LIVE_CALL_ROUTING_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesLiveCallRoutingPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_on_call_role_data_attributes_live_call_routing_permissions_item(
    value: str | None,
) -> NewOnCallRoleDataAttributesLiveCallRoutingPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_LIVE_CALL_ROUTING_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesLiveCallRoutingPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_LIVE_CALL_ROUTING_PERMISSIONS_ITEM_VALUES!r}"
    )
