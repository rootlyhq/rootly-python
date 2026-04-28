from typing import Literal, cast

NewRoleDataAttributesEdgeConnectorPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_EDGE_CONNECTOR_PERMISSIONS_ITEM_VALUES: set[
    NewRoleDataAttributesEdgeConnectorPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_edge_connector_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesEdgeConnectorPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_EDGE_CONNECTOR_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesEdgeConnectorPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_EDGE_CONNECTOR_PERMISSIONS_ITEM_VALUES!r}"
    )
