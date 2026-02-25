from typing import Literal, cast

OnCallRoleServicesPermissionsItem = Literal["create", "delete", "read", "update"]

ON_CALL_ROLE_SERVICES_PERMISSIONS_ITEM_VALUES: set[OnCallRoleServicesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_on_call_role_services_permissions_item(value: str | None) -> OnCallRoleServicesPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_SERVICES_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleServicesPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_SERVICES_PERMISSIONS_ITEM_VALUES!r}")
