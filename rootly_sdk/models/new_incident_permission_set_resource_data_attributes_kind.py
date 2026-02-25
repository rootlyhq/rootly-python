from typing import Literal, cast

NewIncidentPermissionSetResourceDataAttributesKind = Literal["incident_types", "severities", "statuses", "sub_statuses"]

NEW_INCIDENT_PERMISSION_SET_RESOURCE_DATA_ATTRIBUTES_KIND_VALUES: set[
    NewIncidentPermissionSetResourceDataAttributesKind
] = {
    "incident_types",
    "severities",
    "statuses",
    "sub_statuses",
}


def check_new_incident_permission_set_resource_data_attributes_kind(
    value: str | None,
) -> NewIncidentPermissionSetResourceDataAttributesKind | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_PERMISSION_SET_RESOURCE_DATA_ATTRIBUTES_KIND_VALUES:
        return cast(NewIncidentPermissionSetResourceDataAttributesKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_PERMISSION_SET_RESOURCE_DATA_ATTRIBUTES_KIND_VALUES!r}"
    )
