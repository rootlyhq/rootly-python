from typing import Literal, cast

IncidentRoleTaskResponseDataType = Literal["incident_role_tasks"]

INCIDENT_ROLE_TASK_RESPONSE_DATA_TYPE_VALUES: set[IncidentRoleTaskResponseDataType] = {
    "incident_role_tasks",
}


def check_incident_role_task_response_data_type(value: str | None) -> IncidentRoleTaskResponseDataType | None:
    if value is None:
        return None
    if value in INCIDENT_ROLE_TASK_RESPONSE_DATA_TYPE_VALUES:
        return cast(IncidentRoleTaskResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_ROLE_TASK_RESPONSE_DATA_TYPE_VALUES!r}")
