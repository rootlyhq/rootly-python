from typing import Literal, cast

IncidentPermissionSetResponseDataType = Literal["incident_permission_sets"]

INCIDENT_PERMISSION_SET_RESPONSE_DATA_TYPE_VALUES: set[IncidentPermissionSetResponseDataType] = {
    "incident_permission_sets",
}


def check_incident_permission_set_response_data_type(value: str | None) -> IncidentPermissionSetResponseDataType | None:
    if value is None:
        return None
    if value in INCIDENT_PERMISSION_SET_RESPONSE_DATA_TYPE_VALUES:
        return cast(IncidentPermissionSetResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_PERMISSION_SET_RESPONSE_DATA_TYPE_VALUES!r}"
    )
