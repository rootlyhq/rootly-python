from typing import Literal, cast

OnCallRoleScheduleOverridePermissionsItem = Literal["create", "update"]

ON_CALL_ROLE_SCHEDULE_OVERRIDE_PERMISSIONS_ITEM_VALUES: set[OnCallRoleScheduleOverridePermissionsItem] = {
    "create",
    "update",
}


def check_on_call_role_schedule_override_permissions_item(
    value: str | None,
) -> OnCallRoleScheduleOverridePermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_SCHEDULE_OVERRIDE_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleScheduleOverridePermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_SCHEDULE_OVERRIDE_PERMISSIONS_ITEM_VALUES!r}"
    )
