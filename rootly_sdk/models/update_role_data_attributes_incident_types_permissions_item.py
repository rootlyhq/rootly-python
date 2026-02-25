from typing import Literal, cast

UpdateRoleDataAttributesIncidentTypesPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_INCIDENT_TYPES_PERMISSIONS_ITEM_VALUES: set[
    UpdateRoleDataAttributesIncidentTypesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_incident_types_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesIncidentTypesPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_INCIDENT_TYPES_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesIncidentTypesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_INCIDENT_TYPES_PERMISSIONS_ITEM_VALUES!r}"
    )
