from typing import Literal, cast

UpdateRoleDataAttributesIncidentCausesPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_INCIDENT_CAUSES_PERMISSIONS_ITEM_VALUES: set[
    UpdateRoleDataAttributesIncidentCausesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_incident_causes_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesIncidentCausesPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_INCIDENT_CAUSES_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesIncidentCausesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_INCIDENT_CAUSES_PERMISSIONS_ITEM_VALUES!r}"
    )
