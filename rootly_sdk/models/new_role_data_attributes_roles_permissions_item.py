from typing import Literal, cast

NewRoleDataAttributesRolesPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_ROLES_PERMISSIONS_ITEM_VALUES: set[NewRoleDataAttributesRolesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_roles_permissions_item(value: str | None) -> NewRoleDataAttributesRolesPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_ROLES_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesRolesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_ROLES_PERMISSIONS_ITEM_VALUES!r}"
    )
