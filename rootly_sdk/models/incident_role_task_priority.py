from typing import Literal, cast

IncidentRoleTaskPriority = Literal["high", "low", "medium"]

INCIDENT_ROLE_TASK_PRIORITY_VALUES: set[IncidentRoleTaskPriority] = {
    "high",
    "low",
    "medium",
}


def check_incident_role_task_priority(value: str | None) -> IncidentRoleTaskPriority | None:
    if value is None:
        return None
    if value in INCIDENT_ROLE_TASK_PRIORITY_VALUES:
        return cast(IncidentRoleTaskPriority, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_ROLE_TASK_PRIORITY_VALUES!r}")
