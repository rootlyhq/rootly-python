from typing import Literal

NewRoleDataAttributesStatusPageUpdatesPermissionsType0Item = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_STATUS_PAGE_UPDATES_PERMISSIONS_TYPE_0_ITEM_VALUES: set[
    NewRoleDataAttributesStatusPageUpdatesPermissionsType0Item
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_status_page_updates_permissions_type_0_item(
    value: str | None,
) -> NewRoleDataAttributesStatusPageUpdatesPermissionsType0Item | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_STATUS_PAGE_UPDATES_PERMISSIONS_TYPE_0_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_STATUS_PAGE_UPDATES_PERMISSIONS_TYPE_0_ITEM_VALUES!r}"
    )
