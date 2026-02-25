from typing import Literal, cast

UpdateIncidentPermissionSetDataType = Literal["incident_permission_sets"]

UPDATE_INCIDENT_PERMISSION_SET_DATA_TYPE_VALUES: set[UpdateIncidentPermissionSetDataType] = {
    "incident_permission_sets",
}


def check_update_incident_permission_set_data_type(value: str | None) -> UpdateIncidentPermissionSetDataType | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_PERMISSION_SET_DATA_TYPE_VALUES:
        return cast(UpdateIncidentPermissionSetDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_PERMISSION_SET_DATA_TYPE_VALUES!r}")
