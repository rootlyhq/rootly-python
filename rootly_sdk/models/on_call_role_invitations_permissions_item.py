from typing import Literal, cast

OnCallRoleInvitationsPermissionsItem = Literal["create", "delete", "read", "update"]

ON_CALL_ROLE_INVITATIONS_PERMISSIONS_ITEM_VALUES: set[OnCallRoleInvitationsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_on_call_role_invitations_permissions_item(value: str | None) -> OnCallRoleInvitationsPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_INVITATIONS_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleInvitationsPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_INVITATIONS_PERMISSIONS_ITEM_VALUES!r}")
