from typing import Literal, cast

UpdateRoleDataAttributesIncidentRolesPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_INCIDENT_ROLES_PERMISSIONS_ITEM_VALUES: set[
    UpdateRoleDataAttributesIncidentRolesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_incident_roles_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesIncidentRolesPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_INCIDENT_ROLES_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesIncidentRolesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_INCIDENT_ROLES_PERMISSIONS_ITEM_VALUES!r}"
    )
