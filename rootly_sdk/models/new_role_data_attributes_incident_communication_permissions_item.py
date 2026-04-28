from typing import Literal, cast

NewRoleDataAttributesIncidentCommunicationPermissionsItem = Literal["create", "delete", "read", "send", "update"]

NEW_ROLE_DATA_ATTRIBUTES_INCIDENT_COMMUNICATION_PERMISSIONS_ITEM_VALUES: set[
    NewRoleDataAttributesIncidentCommunicationPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "send",
    "update",
}


def check_new_role_data_attributes_incident_communication_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesIncidentCommunicationPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_INCIDENT_COMMUNICATION_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesIncidentCommunicationPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_INCIDENT_COMMUNICATION_PERMISSIONS_ITEM_VALUES!r}"
    )
