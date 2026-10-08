from typing import Literal

UpdateIncidentRoleTaskDataAttributesPriority = Literal["high", "low", "medium"]

UPDATE_INCIDENT_ROLE_TASK_DATA_ATTRIBUTES_PRIORITY_VALUES: set[UpdateIncidentRoleTaskDataAttributesPriority] = {
    "high",
    "low",
    "medium",
}


def check_update_incident_role_task_data_attributes_priority(
    value: str | None,
) -> UpdateIncidentRoleTaskDataAttributesPriority | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_ROLE_TASK_DATA_ATTRIBUTES_PRIORITY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_ROLE_TASK_DATA_ATTRIBUTES_PRIORITY_VALUES!r}"
    )
