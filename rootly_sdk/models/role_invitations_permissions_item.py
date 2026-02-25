from typing import Literal, cast

RoleInvitationsPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_INVITATIONS_PERMISSIONS_ITEM_VALUES: set[RoleInvitationsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_invitations_permissions_item(value: str | None) -> RoleInvitationsPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_INVITATIONS_PERMISSIONS_ITEM_VALUES:
        return cast(RoleInvitationsPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_INVITATIONS_PERMISSIONS_ITEM_VALUES!r}")
