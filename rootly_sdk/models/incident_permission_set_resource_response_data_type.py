from typing import Literal, cast

IncidentPermissionSetResourceResponseDataType = Literal["incident_permission_set_resources"]

INCIDENT_PERMISSION_SET_RESOURCE_RESPONSE_DATA_TYPE_VALUES: set[IncidentPermissionSetResourceResponseDataType] = {
    "incident_permission_set_resources",
}


def check_incident_permission_set_resource_response_data_type(
    value: str | None,
) -> IncidentPermissionSetResourceResponseDataType | None:
    if value is None:
        return None
    if value in INCIDENT_PERMISSION_SET_RESOURCE_RESPONSE_DATA_TYPE_VALUES:
        return cast(IncidentPermissionSetResourceResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_PERMISSION_SET_RESOURCE_RESPONSE_DATA_TYPE_VALUES!r}"
    )
