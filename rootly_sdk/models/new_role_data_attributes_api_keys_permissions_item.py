from typing import Literal, cast

NewRoleDataAttributesApiKeysPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_API_KEYS_PERMISSIONS_ITEM_VALUES: set[NewRoleDataAttributesApiKeysPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_api_keys_permissions_item(value: str | None) -> NewRoleDataAttributesApiKeysPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_API_KEYS_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesApiKeysPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_API_KEYS_PERMISSIONS_ITEM_VALUES!r}"
    )
