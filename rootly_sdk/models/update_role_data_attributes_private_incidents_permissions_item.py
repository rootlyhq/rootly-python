from typing import Literal, cast

UpdateRoleDataAttributesPrivateIncidentsPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_PRIVATE_INCIDENTS_PERMISSIONS_ITEM_VALUES: set[
    UpdateRoleDataAttributesPrivateIncidentsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_private_incidents_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesPrivateIncidentsPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_PRIVATE_INCIDENTS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesPrivateIncidentsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_PRIVATE_INCIDENTS_PERMISSIONS_ITEM_VALUES!r}"
    )
