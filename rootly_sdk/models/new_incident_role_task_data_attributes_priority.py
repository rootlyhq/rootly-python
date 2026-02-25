from typing import Literal, cast

NewIncidentRoleTaskDataAttributesPriority = Literal["high", "low", "medium"]

NEW_INCIDENT_ROLE_TASK_DATA_ATTRIBUTES_PRIORITY_VALUES: set[NewIncidentRoleTaskDataAttributesPriority] = {
    "high",
    "low",
    "medium",
}


def check_new_incident_role_task_data_attributes_priority(
    value: str | None,
) -> NewIncidentRoleTaskDataAttributesPriority | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_ROLE_TASK_DATA_ATTRIBUTES_PRIORITY_VALUES:
        return cast(NewIncidentRoleTaskDataAttributesPriority, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_ROLE_TASK_DATA_ATTRIBUTES_PRIORITY_VALUES!r}"
    )
