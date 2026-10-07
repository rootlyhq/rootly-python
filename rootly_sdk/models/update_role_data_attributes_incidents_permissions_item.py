from typing import Literal

UpdateRoleDataAttributesIncidentsPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_INCIDENTS_PERMISSIONS_ITEM_VALUES: set[UpdateRoleDataAttributesIncidentsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_incidents_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesIncidentsPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_INCIDENTS_PERMISSIONS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_INCIDENTS_PERMISSIONS_ITEM_VALUES!r}"
    )
