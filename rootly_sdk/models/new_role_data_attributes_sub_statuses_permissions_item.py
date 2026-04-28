from typing import Literal, cast

NewRoleDataAttributesSubStatusesPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_SUB_STATUSES_PERMISSIONS_ITEM_VALUES: set[NewRoleDataAttributesSubStatusesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_sub_statuses_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesSubStatusesPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_SUB_STATUSES_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesSubStatusesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_SUB_STATUSES_PERMISSIONS_ITEM_VALUES!r}"
    )
