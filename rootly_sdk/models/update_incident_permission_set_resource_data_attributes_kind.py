from typing import Literal

UpdateIncidentPermissionSetResourceDataAttributesKind = Literal[
    "incident_types", "severities", "statuses", "sub_statuses"
]

UPDATE_INCIDENT_PERMISSION_SET_RESOURCE_DATA_ATTRIBUTES_KIND_VALUES: set[
    UpdateIncidentPermissionSetResourceDataAttributesKind
] = {
    "incident_types",
    "severities",
    "statuses",
    "sub_statuses",
}


def check_update_incident_permission_set_resource_data_attributes_kind(
    value: str | None,
) -> UpdateIncidentPermissionSetResourceDataAttributesKind | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_PERMISSION_SET_RESOURCE_DATA_ATTRIBUTES_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_PERMISSION_SET_RESOURCE_DATA_ATTRIBUTES_KIND_VALUES!r}"
    )
