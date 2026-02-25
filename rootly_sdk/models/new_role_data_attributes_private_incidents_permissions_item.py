from typing import Literal, cast

NewRoleDataAttributesPrivateIncidentsPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_PRIVATE_INCIDENTS_PERMISSIONS_ITEM_VALUES: set[
    NewRoleDataAttributesPrivateIncidentsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_private_incidents_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesPrivateIncidentsPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_PRIVATE_INCIDENTS_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesPrivateIncidentsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_PRIVATE_INCIDENTS_PERMISSIONS_ITEM_VALUES!r}"
    )
