from typing import Literal, cast

UpdateRoleDataAttributesInvitationsPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_INVITATIONS_PERMISSIONS_ITEM_VALUES: set[
    UpdateRoleDataAttributesInvitationsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_invitations_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesInvitationsPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_INVITATIONS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesInvitationsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_INVITATIONS_PERMISSIONS_ITEM_VALUES!r}"
    )
