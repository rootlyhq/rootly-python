from typing import Literal, cast

UpdateIncidentPermissionSetBooleanDataAttributesKind = Literal[
    "assign_incident_roles",
    "create_communications",
    "delete_communications",
    "invite_subscribers",
    "modify_custom_fields",
    "publish_to_status_page",
    "read_communications",
    "send_communications",
    "trigger_workflows",
    "update_communications",
    "update_summary",
    "update_timeline",
]

UPDATE_INCIDENT_PERMISSION_SET_BOOLEAN_DATA_ATTRIBUTES_KIND_VALUES: set[
    UpdateIncidentPermissionSetBooleanDataAttributesKind
] = {
    "assign_incident_roles",
    "create_communications",
    "delete_communications",
    "invite_subscribers",
    "modify_custom_fields",
    "publish_to_status_page",
    "read_communications",
    "send_communications",
    "trigger_workflows",
    "update_communications",
    "update_summary",
    "update_timeline",
}


def check_update_incident_permission_set_boolean_data_attributes_kind(
    value: str | None,
) -> UpdateIncidentPermissionSetBooleanDataAttributesKind | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_PERMISSION_SET_BOOLEAN_DATA_ATTRIBUTES_KIND_VALUES:
        return cast(UpdateIncidentPermissionSetBooleanDataAttributesKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_PERMISSION_SET_BOOLEAN_DATA_ATTRIBUTES_KIND_VALUES!r}"
    )
