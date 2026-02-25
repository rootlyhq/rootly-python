from typing import Literal, cast

NewOnCallRoleDataAttributesOnCallRolesPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ON_CALL_ROLES_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesOnCallRolesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_on_call_role_data_attributes_on_call_roles_permissions_item(
    value: str | None,
) -> NewOnCallRoleDataAttributesOnCallRolesPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ON_CALL_ROLES_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesOnCallRolesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ON_CALL_ROLES_PERMISSIONS_ITEM_VALUES!r}"
    )
