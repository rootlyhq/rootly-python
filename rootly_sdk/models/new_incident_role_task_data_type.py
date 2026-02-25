from typing import Literal, cast

NewIncidentRoleTaskDataType = Literal["incident_role_tasks"]

NEW_INCIDENT_ROLE_TASK_DATA_TYPE_VALUES: set[NewIncidentRoleTaskDataType] = {
    "incident_role_tasks",
}


def check_new_incident_role_task_data_type(value: str | None) -> NewIncidentRoleTaskDataType | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_ROLE_TASK_DATA_TYPE_VALUES:
        return cast(NewIncidentRoleTaskDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_ROLE_TASK_DATA_TYPE_VALUES!r}")
