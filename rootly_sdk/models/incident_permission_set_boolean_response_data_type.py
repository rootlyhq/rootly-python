from typing import Literal, cast

IncidentPermissionSetBooleanResponseDataType = Literal["incident_permission_set_booleans"]

INCIDENT_PERMISSION_SET_BOOLEAN_RESPONSE_DATA_TYPE_VALUES: set[IncidentPermissionSetBooleanResponseDataType] = {
    "incident_permission_set_booleans",
}


def check_incident_permission_set_boolean_response_data_type(
    value: str | None,
) -> IncidentPermissionSetBooleanResponseDataType | None:
    if value is None:
        return None
    if value in INCIDENT_PERMISSION_SET_BOOLEAN_RESPONSE_DATA_TYPE_VALUES:
        return cast(IncidentPermissionSetBooleanResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_PERMISSION_SET_BOOLEAN_RESPONSE_DATA_TYPE_VALUES!r}"
    )
