from typing import Literal, cast

NewOnCallRoleDataAttributesScheduleOverridePermissionsItem = Literal["create", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_SCHEDULE_OVERRIDE_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesScheduleOverridePermissionsItem
] = {
    "create",
    "update",
}


def check_new_on_call_role_data_attributes_schedule_override_permissions_item(
    value: str | None,
) -> NewOnCallRoleDataAttributesScheduleOverridePermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_SCHEDULE_OVERRIDE_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesScheduleOverridePermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_SCHEDULE_OVERRIDE_PERMISSIONS_ITEM_VALUES!r}"
    )
