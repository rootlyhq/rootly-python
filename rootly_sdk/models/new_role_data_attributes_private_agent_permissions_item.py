from typing import Literal

NewRoleDataAttributesPrivateAgentPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_PRIVATE_AGENT_PERMISSIONS_ITEM_VALUES: set[
    NewRoleDataAttributesPrivateAgentPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_private_agent_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesPrivateAgentPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_PRIVATE_AGENT_PERMISSIONS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_PRIVATE_AGENT_PERMISSIONS_ITEM_VALUES!r}"
    )
