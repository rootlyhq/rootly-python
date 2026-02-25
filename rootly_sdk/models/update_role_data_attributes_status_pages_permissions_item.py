from typing import Literal, cast

UpdateRoleDataAttributesStatusPagesPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_STATUS_PAGES_PERMISSIONS_ITEM_VALUES: set[
    UpdateRoleDataAttributesStatusPagesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_status_pages_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesStatusPagesPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_STATUS_PAGES_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesStatusPagesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_STATUS_PAGES_PERMISSIONS_ITEM_VALUES!r}"
    )
