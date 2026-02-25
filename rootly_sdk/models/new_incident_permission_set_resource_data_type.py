from typing import Literal, cast

NewIncidentPermissionSetResourceDataType = Literal["incident_permission_set_resources"]

NEW_INCIDENT_PERMISSION_SET_RESOURCE_DATA_TYPE_VALUES: set[NewIncidentPermissionSetResourceDataType] = {
    "incident_permission_set_resources",
}


def check_new_incident_permission_set_resource_data_type(value: str | None) -> NewIncidentPermissionSetResourceDataType | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_PERMISSION_SET_RESOURCE_DATA_TYPE_VALUES:
        return cast(NewIncidentPermissionSetResourceDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_PERMISSION_SET_RESOURCE_DATA_TYPE_VALUES!r}"
    )
