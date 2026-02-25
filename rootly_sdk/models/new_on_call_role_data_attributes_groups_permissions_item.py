from typing import Literal, cast

NewOnCallRoleDataAttributesGroupsPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_GROUPS_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesGroupsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_on_call_role_data_attributes_groups_permissions_item(
    value: str | None,
) -> NewOnCallRoleDataAttributesGroupsPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_GROUPS_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesGroupsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_GROUPS_PERMISSIONS_ITEM_VALUES!r}"
    )
