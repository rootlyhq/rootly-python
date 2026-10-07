from typing import Literal

UpdateRoleDataAttributesStatusPageUpdatesPermissionsType0Item = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_STATUS_PAGE_UPDATES_PERMISSIONS_TYPE_0_ITEM_VALUES: set[
    UpdateRoleDataAttributesStatusPageUpdatesPermissionsType0Item
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_status_page_updates_permissions_type_0_item(
    value: str | None,
) -> UpdateRoleDataAttributesStatusPageUpdatesPermissionsType0Item | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_STATUS_PAGE_UPDATES_PERMISSIONS_TYPE_0_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_STATUS_PAGE_UPDATES_PERMISSIONS_TYPE_0_ITEM_VALUES!r}"
    )
