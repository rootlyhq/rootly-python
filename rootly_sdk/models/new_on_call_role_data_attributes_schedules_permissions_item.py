from typing import Literal, cast

NewOnCallRoleDataAttributesSchedulesPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_SCHEDULES_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesSchedulesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_on_call_role_data_attributes_schedules_permissions_item(
    value: str | None,
) -> NewOnCallRoleDataAttributesSchedulesPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_SCHEDULES_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesSchedulesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_SCHEDULES_PERMISSIONS_ITEM_VALUES!r}"
    )
