from typing import Literal, cast

UpdateRoleDataAttributesGroupsPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_GROUPS_PERMISSIONS_ITEM_VALUES: set[UpdateRoleDataAttributesGroupsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_groups_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesGroupsPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_GROUPS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesGroupsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_GROUPS_PERMISSIONS_ITEM_VALUES!r}"
    )
