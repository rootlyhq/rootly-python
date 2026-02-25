from typing import Literal, cast

OnCallRoleSchedulesPermissionsItem = Literal["create", "delete", "read", "update"]

ON_CALL_ROLE_SCHEDULES_PERMISSIONS_ITEM_VALUES: set[OnCallRoleSchedulesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_on_call_role_schedules_permissions_item(value: str | None) -> OnCallRoleSchedulesPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_SCHEDULES_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleSchedulesPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_SCHEDULES_PERMISSIONS_ITEM_VALUES!r}")
