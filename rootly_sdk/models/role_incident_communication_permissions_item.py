from typing import Literal, cast

RoleIncidentCommunicationPermissionsItem = Literal["create", "delete", "read", "send", "update"]

ROLE_INCIDENT_COMMUNICATION_PERMISSIONS_ITEM_VALUES: set[RoleIncidentCommunicationPermissionsItem] = {
    "create",
    "delete",
    "read",
    "send",
    "update",
}


def check_role_incident_communication_permissions_item(
    value: str | None,
) -> RoleIncidentCommunicationPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_INCIDENT_COMMUNICATION_PERMISSIONS_ITEM_VALUES:
        return cast(RoleIncidentCommunicationPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROLE_INCIDENT_COMMUNICATION_PERMISSIONS_ITEM_VALUES!r}"
    )
