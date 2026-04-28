from typing import Literal, cast

UpdateRoleDataAttributesPagingPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_PAGING_PERMISSIONS_ITEM_VALUES: set[UpdateRoleDataAttributesPagingPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_paging_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesPagingPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_PAGING_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesPagingPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_PAGING_PERMISSIONS_ITEM_VALUES!r}"
    )
