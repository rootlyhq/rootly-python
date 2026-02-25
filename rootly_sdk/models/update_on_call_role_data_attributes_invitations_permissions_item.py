from typing import Literal, cast

UpdateOnCallRoleDataAttributesInvitationsPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_INVITATIONS_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesInvitationsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_on_call_role_data_attributes_invitations_permissions_item(
    value: str | None,
) -> UpdateOnCallRoleDataAttributesInvitationsPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_INVITATIONS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateOnCallRoleDataAttributesInvitationsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_INVITATIONS_PERMISSIONS_ITEM_VALUES!r}"
    )
