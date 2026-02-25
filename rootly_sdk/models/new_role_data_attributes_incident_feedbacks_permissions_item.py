from typing import Literal, cast

NewRoleDataAttributesIncidentFeedbacksPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_INCIDENT_FEEDBACKS_PERMISSIONS_ITEM_VALUES: set[
    NewRoleDataAttributesIncidentFeedbacksPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_incident_feedbacks_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesIncidentFeedbacksPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_INCIDENT_FEEDBACKS_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesIncidentFeedbacksPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_INCIDENT_FEEDBACKS_PERMISSIONS_ITEM_VALUES!r}"
    )
