from typing import Literal, cast

UpdateOnCallRoleDataAttributesApiKeysPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_API_KEYS_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesApiKeysPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_on_call_role_data_attributes_api_keys_permissions_item(
    value: str | None,
) -> UpdateOnCallRoleDataAttributesApiKeysPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_API_KEYS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateOnCallRoleDataAttributesApiKeysPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_API_KEYS_PERMISSIONS_ITEM_VALUES!r}"
    )
