from typing import Literal, cast

UpdateRoleDataAttributesRolesPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_ROLES_PERMISSIONS_ITEM_VALUES: set[UpdateRoleDataAttributesRolesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_roles_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesRolesPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_ROLES_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesRolesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_ROLES_PERMISSIONS_ITEM_VALUES!r}"
    )
