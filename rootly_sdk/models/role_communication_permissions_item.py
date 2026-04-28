from typing import Literal, cast

RoleCommunicationPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_COMMUNICATION_PERMISSIONS_ITEM_VALUES: set[RoleCommunicationPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_communication_permissions_item(value: str | None) -> RoleCommunicationPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_COMMUNICATION_PERMISSIONS_ITEM_VALUES:
        return cast(RoleCommunicationPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_COMMUNICATION_PERMISSIONS_ITEM_VALUES!r}")
