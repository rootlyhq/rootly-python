from typing import Literal, cast

UpdateIncidentRoleDataType = Literal["incident_roles"]

UPDATE_INCIDENT_ROLE_DATA_TYPE_VALUES: set[UpdateIncidentRoleDataType] = {
    "incident_roles",
}


def check_update_incident_role_data_type(value: str | None) -> UpdateIncidentRoleDataType | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_ROLE_DATA_TYPE_VALUES:
        return cast(UpdateIncidentRoleDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_ROLE_DATA_TYPE_VALUES!r}")
