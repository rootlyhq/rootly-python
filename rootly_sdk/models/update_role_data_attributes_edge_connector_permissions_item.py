from typing import Literal, cast

UpdateRoleDataAttributesEdgeConnectorPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_EDGE_CONNECTOR_PERMISSIONS_ITEM_VALUES: set[
    UpdateRoleDataAttributesEdgeConnectorPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_edge_connector_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesEdgeConnectorPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_EDGE_CONNECTOR_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesEdgeConnectorPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_EDGE_CONNECTOR_PERMISSIONS_ITEM_VALUES!r}"
    )
