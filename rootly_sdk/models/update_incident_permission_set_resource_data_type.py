from typing import Literal, cast

UpdateIncidentPermissionSetResourceDataType = Literal["incident_permission_set_resources"]

UPDATE_INCIDENT_PERMISSION_SET_RESOURCE_DATA_TYPE_VALUES: set[UpdateIncidentPermissionSetResourceDataType] = {
    "incident_permission_set_resources",
}


def check_update_incident_permission_set_resource_data_type(
    value: str | None,
) -> UpdateIncidentPermissionSetResourceDataType | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_PERMISSION_SET_RESOURCE_DATA_TYPE_VALUES:
        return cast(UpdateIncidentPermissionSetResourceDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_PERMISSION_SET_RESOURCE_DATA_TYPE_VALUES!r}"
    )
