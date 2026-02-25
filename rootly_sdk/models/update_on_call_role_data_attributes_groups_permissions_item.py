from typing import Literal, cast

UpdateOnCallRoleDataAttributesGroupsPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_GROUPS_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesGroupsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_on_call_role_data_attributes_groups_permissions_item(
    value: str | None,
) -> UpdateOnCallRoleDataAttributesGroupsPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_GROUPS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateOnCallRoleDataAttributesGroupsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_GROUPS_PERMISSIONS_ITEM_VALUES!r}"
    )
