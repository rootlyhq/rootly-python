from typing import Literal, cast

NewOnCallRoleDataAttributesCatalogsPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_CATALOGS_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesCatalogsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_on_call_role_data_attributes_catalogs_permissions_item(
    value: str | None,
) -> NewOnCallRoleDataAttributesCatalogsPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_CATALOGS_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesCatalogsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_CATALOGS_PERMISSIONS_ITEM_VALUES!r}"
    )
