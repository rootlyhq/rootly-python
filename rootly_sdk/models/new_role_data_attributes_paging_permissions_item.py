from typing import Literal, cast

NewRoleDataAttributesPagingPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_PAGING_PERMISSIONS_ITEM_VALUES: set[NewRoleDataAttributesPagingPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_paging_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesPagingPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_PAGING_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesPagingPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_PAGING_PERMISSIONS_ITEM_VALUES!r}"
    )
