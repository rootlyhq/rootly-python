from typing import Literal, cast

RoleIncidentFeedbacksPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_INCIDENT_FEEDBACKS_PERMISSIONS_ITEM_VALUES: set[RoleIncidentFeedbacksPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_incident_feedbacks_permissions_item(value: str | None) -> RoleIncidentFeedbacksPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_INCIDENT_FEEDBACKS_PERMISSIONS_ITEM_VALUES:
        return cast(RoleIncidentFeedbacksPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_INCIDENT_FEEDBACKS_PERMISSIONS_ITEM_VALUES!r}")
