from typing import Literal, cast

NewIncidentRoleDataType = Literal["incident_roles"]

NEW_INCIDENT_ROLE_DATA_TYPE_VALUES: set[NewIncidentRoleDataType] = {
    "incident_roles",
}


def check_new_incident_role_data_type(value: str | None) -> NewIncidentRoleDataType | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_ROLE_DATA_TYPE_VALUES:
        return cast(NewIncidentRoleDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_ROLE_DATA_TYPE_VALUES!r}")
