from typing import Literal, cast

NewRoleDataAttributesIncidentCausesPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_INCIDENT_CAUSES_PERMISSIONS_ITEM_VALUES: set[
    NewRoleDataAttributesIncidentCausesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_incident_causes_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesIncidentCausesPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_INCIDENT_CAUSES_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesIncidentCausesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_INCIDENT_CAUSES_PERMISSIONS_ITEM_VALUES!r}"
    )
