from typing import Literal, cast

UpdateRoleDataAttributesSubStatusesPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_SUB_STATUSES_PERMISSIONS_ITEM_VALUES: set[
    UpdateRoleDataAttributesSubStatusesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_sub_statuses_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesSubStatusesPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_SUB_STATUSES_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesSubStatusesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_SUB_STATUSES_PERMISSIONS_ITEM_VALUES!r}"
    )
