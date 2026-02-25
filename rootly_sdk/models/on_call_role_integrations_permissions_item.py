from typing import Literal, cast

OnCallRoleIntegrationsPermissionsItem = Literal["create", "delete", "read", "update"]

ON_CALL_ROLE_INTEGRATIONS_PERMISSIONS_ITEM_VALUES: set[OnCallRoleIntegrationsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_on_call_role_integrations_permissions_item(value: str | None) -> OnCallRoleIntegrationsPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_INTEGRATIONS_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleIntegrationsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_INTEGRATIONS_PERMISSIONS_ITEM_VALUES!r}"
    )
