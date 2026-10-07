from typing import Literal

UpdateOnCallRoleDataAttributesCatalogsPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_CATALOGS_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesCatalogsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_on_call_role_data_attributes_catalogs_permissions_item(
    value: str | None,
) -> UpdateOnCallRoleDataAttributesCatalogsPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_CATALOGS_PERMISSIONS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_CATALOGS_PERMISSIONS_ITEM_VALUES!r}"
    )
