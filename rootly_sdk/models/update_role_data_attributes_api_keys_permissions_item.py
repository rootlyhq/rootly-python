from typing import Literal, cast

UpdateRoleDataAttributesApiKeysPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_API_KEYS_PERMISSIONS_ITEM_VALUES: set[UpdateRoleDataAttributesApiKeysPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_api_keys_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesApiKeysPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_API_KEYS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesApiKeysPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_API_KEYS_PERMISSIONS_ITEM_VALUES!r}"
    )
