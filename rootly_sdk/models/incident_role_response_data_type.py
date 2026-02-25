from typing import Literal, cast

IncidentRoleResponseDataType = Literal["incident_roles"]

INCIDENT_ROLE_RESPONSE_DATA_TYPE_VALUES: set[IncidentRoleResponseDataType] = {
    "incident_roles",
}


def check_incident_role_response_data_type(value: str | None) -> IncidentRoleResponseDataType | None:
    if value is None:
        return None
    if value in INCIDENT_ROLE_RESPONSE_DATA_TYPE_VALUES:
        return cast(IncidentRoleResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_ROLE_RESPONSE_DATA_TYPE_VALUES!r}")
