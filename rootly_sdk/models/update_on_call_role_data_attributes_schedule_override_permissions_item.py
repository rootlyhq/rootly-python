from typing import Literal, cast

UpdateOnCallRoleDataAttributesScheduleOverridePermissionsItem = Literal["create", "update"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_SCHEDULE_OVERRIDE_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesScheduleOverridePermissionsItem
] = {
    "create",
    "update",
}


def check_update_on_call_role_data_attributes_schedule_override_permissions_item(
    value: str | None,
) -> UpdateOnCallRoleDataAttributesScheduleOverridePermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_SCHEDULE_OVERRIDE_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateOnCallRoleDataAttributesScheduleOverridePermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_SCHEDULE_OVERRIDE_PERMISSIONS_ITEM_VALUES!r}"
    )
