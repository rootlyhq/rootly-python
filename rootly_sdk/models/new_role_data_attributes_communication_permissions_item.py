from typing import Literal, cast

NewRoleDataAttributesCommunicationPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_COMMUNICATION_PERMISSIONS_ITEM_VALUES: set[
    NewRoleDataAttributesCommunicationPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_communication_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesCommunicationPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_COMMUNICATION_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesCommunicationPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_COMMUNICATION_PERMISSIONS_ITEM_VALUES!r}"
    )
