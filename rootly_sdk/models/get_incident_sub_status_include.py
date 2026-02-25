from typing import Literal, cast

GetIncidentSubStatusInclude = Literal["assigned_by_user", "sub_status"]

GET_INCIDENT_SUB_STATUS_INCLUDE_VALUES: set[GetIncidentSubStatusInclude] = {
    "assigned_by_user",
    "sub_status",
}


def check_get_incident_sub_status_include(value: str | None) -> GetIncidentSubStatusInclude | None:
    if value is None:
        return None
    if value in GET_INCIDENT_SUB_STATUS_INCLUDE_VALUES:
        return cast(GetIncidentSubStatusInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_INCIDENT_SUB_STATUS_INCLUDE_VALUES!r}")
