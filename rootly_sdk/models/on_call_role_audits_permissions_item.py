from typing import Literal, cast

OnCallRoleAuditsPermissionsItem = Literal["create", "delete", "read", "update"]

ON_CALL_ROLE_AUDITS_PERMISSIONS_ITEM_VALUES: set[OnCallRoleAuditsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_on_call_role_audits_permissions_item(value: str | None) -> OnCallRoleAuditsPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_AUDITS_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleAuditsPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_AUDITS_PERMISSIONS_ITEM_VALUES!r}")
