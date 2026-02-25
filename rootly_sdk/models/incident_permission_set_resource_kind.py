from typing import Literal, cast

IncidentPermissionSetResourceKind = Literal["incident_types", "severities", "statuses", "sub_statuses"]

INCIDENT_PERMISSION_SET_RESOURCE_KIND_VALUES: set[IncidentPermissionSetResourceKind] = {
    "incident_types",
    "severities",
    "statuses",
    "sub_statuses",
}


def check_incident_permission_set_resource_kind(value: str | None) -> IncidentPermissionSetResourceKind | None:
    if value is None:
        return None
    if value in INCIDENT_PERMISSION_SET_RESOURCE_KIND_VALUES:
        return cast(IncidentPermissionSetResourceKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_PERMISSION_SET_RESOURCE_KIND_VALUES!r}")
