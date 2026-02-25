from typing import Literal, cast

NewRoleDataAttributesFunctionalitiesPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_FUNCTIONALITIES_PERMISSIONS_ITEM_VALUES: set[
    NewRoleDataAttributesFunctionalitiesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_functionalities_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesFunctionalitiesPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_FUNCTIONALITIES_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesFunctionalitiesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_FUNCTIONALITIES_PERMISSIONS_ITEM_VALUES!r}"
    )
