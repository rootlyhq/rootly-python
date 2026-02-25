from typing import Literal, cast

NewOnCallRoleDataAttributesApiKeysPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_API_KEYS_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesApiKeysPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_on_call_role_data_attributes_api_keys_permissions_item(
    value: str | None,
) -> NewOnCallRoleDataAttributesApiKeysPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_API_KEYS_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesApiKeysPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_API_KEYS_PERMISSIONS_ITEM_VALUES!r}"
    )
