from typing import Literal, cast

NewIncidentPermissionSetDataType = Literal["incident_permission_sets"]

NEW_INCIDENT_PERMISSION_SET_DATA_TYPE_VALUES: set[NewIncidentPermissionSetDataType] = {
    "incident_permission_sets",
}


def check_new_incident_permission_set_data_type(value: str | None) -> NewIncidentPermissionSetDataType | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_PERMISSION_SET_DATA_TYPE_VALUES:
        return cast(NewIncidentPermissionSetDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_PERMISSION_SET_DATA_TYPE_VALUES!r}")
