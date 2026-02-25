from typing import Literal, cast

OnCallRoleLiveCallRoutingPermissionsItem = Literal["create", "delete", "read", "update"]

ON_CALL_ROLE_LIVE_CALL_ROUTING_PERMISSIONS_ITEM_VALUES: set[OnCallRoleLiveCallRoutingPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_on_call_role_live_call_routing_permissions_item(value: str | None) -> OnCallRoleLiveCallRoutingPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_LIVE_CALL_ROUTING_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleLiveCallRoutingPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_LIVE_CALL_ROUTING_PERMISSIONS_ITEM_VALUES!r}"
    )
