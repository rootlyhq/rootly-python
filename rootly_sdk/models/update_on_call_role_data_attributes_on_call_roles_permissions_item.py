from typing import Literal, cast

UpdateOnCallRoleDataAttributesOnCallRolesPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ON_CALL_ROLES_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesOnCallRolesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_on_call_role_data_attributes_on_call_roles_permissions_item(
    value: str | None,
) -> UpdateOnCallRoleDataAttributesOnCallRolesPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ON_CALL_ROLES_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateOnCallRoleDataAttributesOnCallRolesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ON_CALL_ROLES_PERMISSIONS_ITEM_VALUES!r}"
    )
