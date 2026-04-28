from typing import Literal, cast

UpdateRoleDataAttributesCatalogsPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_CATALOGS_PERMISSIONS_ITEM_VALUES: set[UpdateRoleDataAttributesCatalogsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_catalogs_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesCatalogsPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_CATALOGS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesCatalogsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_CATALOGS_PERMISSIONS_ITEM_VALUES!r}"
    )
