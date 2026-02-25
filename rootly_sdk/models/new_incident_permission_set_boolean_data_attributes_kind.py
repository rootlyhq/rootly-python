from typing import Literal, cast

NewIncidentPermissionSetBooleanDataAttributesKind = Literal[
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

NEW_INCIDENT_PERMISSION_SET_BOOLEAN_DATA_ATTRIBUTES_KIND_VALUES: set[
    NewIncidentPermissionSetBooleanDataAttributesKind
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


def check_new_incident_permission_set_boolean_data_attributes_kind(
    value: str | None,
) -> NewIncidentPermissionSetBooleanDataAttributesKind | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_PERMISSION_SET_BOOLEAN_DATA_ATTRIBUTES_KIND_VALUES:
        return cast(NewIncidentPermissionSetBooleanDataAttributesKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_PERMISSION_SET_BOOLEAN_DATA_ATTRIBUTES_KIND_VALUES!r}"
    )
