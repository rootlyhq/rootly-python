from typing import Literal, cast

NewRoleDataAttributesStatusPagesPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_STATUS_PAGES_PERMISSIONS_ITEM_VALUES: set[NewRoleDataAttributesStatusPagesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_status_pages_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesStatusPagesPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_STATUS_PAGES_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesStatusPagesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_STATUS_PAGES_PERMISSIONS_ITEM_VALUES!r}"
    )
