from typing import Literal, cast

UpdateIncidentRoleTaskDataType = Literal["incident_role_tasks"]

UPDATE_INCIDENT_ROLE_TASK_DATA_TYPE_VALUES: set[UpdateIncidentRoleTaskDataType] = {
    "incident_role_tasks",
}


def check_update_incident_role_task_data_type(value: str | None) -> UpdateIncidentRoleTaskDataType | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_ROLE_TASK_DATA_TYPE_VALUES:
        return cast(UpdateIncidentRoleTaskDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_ROLE_TASK_DATA_TYPE_VALUES!r}")
