from typing import Literal, cast

NewIncidentPermissionSetBooleanDataType = Literal["incident_permission_set_booleans"]

NEW_INCIDENT_PERMISSION_SET_BOOLEAN_DATA_TYPE_VALUES: set[NewIncidentPermissionSetBooleanDataType] = {
    "incident_permission_set_booleans",
}


def check_new_incident_permission_set_boolean_data_type(value: str | None) -> NewIncidentPermissionSetBooleanDataType | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_PERMISSION_SET_BOOLEAN_DATA_TYPE_VALUES:
        return cast(NewIncidentPermissionSetBooleanDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_PERMISSION_SET_BOOLEAN_DATA_TYPE_VALUES!r}"
    )
