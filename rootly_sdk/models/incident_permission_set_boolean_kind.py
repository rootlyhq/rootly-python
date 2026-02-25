from typing import Literal, cast

IncidentPermissionSetBooleanKind = Literal[
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

INCIDENT_PERMISSION_SET_BOOLEAN_KIND_VALUES: set[IncidentPermissionSetBooleanKind] = {
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


def check_incident_permission_set_boolean_kind(value: str | None) -> IncidentPermissionSetBooleanKind | None:
    if value is None:
        return None
    if value in INCIDENT_PERMISSION_SET_BOOLEAN_KIND_VALUES:
        return cast(IncidentPermissionSetBooleanKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_PERMISSION_SET_BOOLEAN_KIND_VALUES!r}")
