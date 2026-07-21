from typing import Literal, cast

UpdateOnCallRoleDataAttributesFunctionalitiesPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_FUNCTIONALITIES_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesFunctionalitiesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_on_call_role_data_attributes_functionalities_permissions_item(
    value: str | None,
) -> UpdateOnCallRoleDataAttributesFunctionalitiesPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_FUNCTIONALITIES_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateOnCallRoleDataAttributesFunctionalitiesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_FUNCTIONALITIES_PERMISSIONS_ITEM_VALUES!r}"
    )
