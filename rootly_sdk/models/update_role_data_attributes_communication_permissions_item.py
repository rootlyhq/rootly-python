from typing import Literal, cast

UpdateRoleDataAttributesCommunicationPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_COMMUNICATION_PERMISSIONS_ITEM_VALUES: set[
    UpdateRoleDataAttributesCommunicationPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_communication_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesCommunicationPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_COMMUNICATION_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesCommunicationPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_COMMUNICATION_PERMISSIONS_ITEM_VALUES!r}"
    )
