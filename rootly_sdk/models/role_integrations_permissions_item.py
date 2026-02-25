from typing import Literal, cast

RoleIntegrationsPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_INTEGRATIONS_PERMISSIONS_ITEM_VALUES: set[RoleIntegrationsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_integrations_permissions_item(value: str | None) -> RoleIntegrationsPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_INTEGRATIONS_PERMISSIONS_ITEM_VALUES:
        return cast(RoleIntegrationsPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_INTEGRATIONS_PERMISSIONS_ITEM_VALUES!r}")
