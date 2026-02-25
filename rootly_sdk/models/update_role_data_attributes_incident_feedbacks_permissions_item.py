from typing import Literal, cast

UpdateRoleDataAttributesIncidentFeedbacksPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_INCIDENT_FEEDBACKS_PERMISSIONS_ITEM_VALUES: set[
    UpdateRoleDataAttributesIncidentFeedbacksPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_incident_feedbacks_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesIncidentFeedbacksPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_INCIDENT_FEEDBACKS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesIncidentFeedbacksPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_INCIDENT_FEEDBACKS_PERMISSIONS_ITEM_VALUES!r}"
    )
