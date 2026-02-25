from typing import Literal, cast

NewOnCallRoleDataAttributesInvitationsPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_INVITATIONS_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesInvitationsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_on_call_role_data_attributes_invitations_permissions_item(
    value: str | None,
) -> NewOnCallRoleDataAttributesInvitationsPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_INVITATIONS_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesInvitationsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_INVITATIONS_PERMISSIONS_ITEM_VALUES!r}"
    )
