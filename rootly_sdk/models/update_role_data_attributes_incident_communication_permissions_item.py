from typing import Literal, cast

UpdateRoleDataAttributesIncidentCommunicationPermissionsItem = Literal["create", "delete", "read", "send", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_INCIDENT_COMMUNICATION_PERMISSIONS_ITEM_VALUES: set[
    UpdateRoleDataAttributesIncidentCommunicationPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "send",
    "update",
}


def check_update_role_data_attributes_incident_communication_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesIncidentCommunicationPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_INCIDENT_COMMUNICATION_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesIncidentCommunicationPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_INCIDENT_COMMUNICATION_PERMISSIONS_ITEM_VALUES!r}"
    )
