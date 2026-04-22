from typing import Literal, cast

NewRoleDataAttributesCatalogsPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_CATALOGS_PERMISSIONS_ITEM_VALUES: set[NewRoleDataAttributesCatalogsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_catalogs_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesCatalogsPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_CATALOGS_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesCatalogsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_CATALOGS_PERMISSIONS_ITEM_VALUES!r}"
    )
