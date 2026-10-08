from typing import Literal

NewOnCallRoleDataAttributesMembersPermissionsItem = Literal["delete", "read", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_MEMBERS_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesMembersPermissionsItem
] = {
    "delete",
    "read",
    "update",
}


def check_new_on_call_role_data_attributes_members_permissions_item(
    value: str | None,
) -> NewOnCallRoleDataAttributesMembersPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_MEMBERS_PERMISSIONS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_MEMBERS_PERMISSIONS_ITEM_VALUES!r}"
    )
