from typing import Literal

UpdateIncidentPermissionSetBooleanDataType = Literal["incident_permission_set_booleans"]

UPDATE_INCIDENT_PERMISSION_SET_BOOLEAN_DATA_TYPE_VALUES: set[UpdateIncidentPermissionSetBooleanDataType] = {
    "incident_permission_set_booleans",
}


def check_update_incident_permission_set_boolean_data_type(
    value: str | None,
) -> UpdateIncidentPermissionSetBooleanDataType | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_PERMISSION_SET_BOOLEAN_DATA_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_PERMISSION_SET_BOOLEAN_DATA_TYPE_VALUES!r}"
    )
