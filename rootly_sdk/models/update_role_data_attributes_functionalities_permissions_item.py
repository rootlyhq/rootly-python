from typing import Literal, cast

UpdateRoleDataAttributesFunctionalitiesPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_FUNCTIONALITIES_PERMISSIONS_ITEM_VALUES: set[
    UpdateRoleDataAttributesFunctionalitiesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_functionalities_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesFunctionalitiesPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_FUNCTIONALITIES_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesFunctionalitiesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_FUNCTIONALITIES_PERMISSIONS_ITEM_VALUES!r}"
    )
