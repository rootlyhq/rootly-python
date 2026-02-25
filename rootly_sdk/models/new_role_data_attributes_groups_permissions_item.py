from typing import Literal, cast

NewRoleDataAttributesGroupsPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_GROUPS_PERMISSIONS_ITEM_VALUES: set[NewRoleDataAttributesGroupsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_groups_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesGroupsPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_GROUPS_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesGroupsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_GROUPS_PERMISSIONS_ITEM_VALUES!r}"
    )
