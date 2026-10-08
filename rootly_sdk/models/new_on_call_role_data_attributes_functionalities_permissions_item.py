from typing import Literal

NewOnCallRoleDataAttributesFunctionalitiesPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_FUNCTIONALITIES_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesFunctionalitiesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_on_call_role_data_attributes_functionalities_permissions_item(
    value: str | None,
) -> NewOnCallRoleDataAttributesFunctionalitiesPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_FUNCTIONALITIES_PERMISSIONS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_FUNCTIONALITIES_PERMISSIONS_ITEM_VALUES!r}"
    )
