from typing import Literal, cast

RoleEdgeConnectorPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_EDGE_CONNECTOR_PERMISSIONS_ITEM_VALUES: set[RoleEdgeConnectorPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_edge_connector_permissions_item(value: str | None) -> RoleEdgeConnectorPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_EDGE_CONNECTOR_PERMISSIONS_ITEM_VALUES:
        return cast(RoleEdgeConnectorPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_EDGE_CONNECTOR_PERMISSIONS_ITEM_VALUES!r}")
