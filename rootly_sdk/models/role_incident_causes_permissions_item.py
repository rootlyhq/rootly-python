from typing import Literal, cast

RoleIncidentCausesPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_INCIDENT_CAUSES_PERMISSIONS_ITEM_VALUES: set[RoleIncidentCausesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_incident_causes_permissions_item(value: str | None) -> RoleIncidentCausesPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_INCIDENT_CAUSES_PERMISSIONS_ITEM_VALUES:
        return cast(RoleIncidentCausesPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_INCIDENT_CAUSES_PERMISSIONS_ITEM_VALUES!r}")
