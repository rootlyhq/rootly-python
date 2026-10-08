from typing import Literal

RolePrivateAgentPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_PRIVATE_AGENT_PERMISSIONS_ITEM_VALUES: set[RolePrivateAgentPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_private_agent_permissions_item(value: str | None) -> RolePrivateAgentPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_PRIVATE_AGENT_PERMISSIONS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_PRIVATE_AGENT_PERMISSIONS_ITEM_VALUES!r}")
