from typing import Literal, cast

NewRoleDataAttributesIncidentTypesPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_INCIDENT_TYPES_PERMISSIONS_ITEM_VALUES: set[
    NewRoleDataAttributesIncidentTypesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_incident_types_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesIncidentTypesPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_INCIDENT_TYPES_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesIncidentTypesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_INCIDENT_TYPES_PERMISSIONS_ITEM_VALUES!r}"
    )
