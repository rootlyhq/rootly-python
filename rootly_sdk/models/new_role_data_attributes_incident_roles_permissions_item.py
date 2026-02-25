from typing import Literal, cast

NewRoleDataAttributesIncidentRolesPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_INCIDENT_ROLES_PERMISSIONS_ITEM_VALUES: set[
    NewRoleDataAttributesIncidentRolesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_incident_roles_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesIncidentRolesPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_INCIDENT_ROLES_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesIncidentRolesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_INCIDENT_ROLES_PERMISSIONS_ITEM_VALUES!r}"
    )
