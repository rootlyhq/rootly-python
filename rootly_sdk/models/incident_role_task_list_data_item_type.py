from typing import Literal, cast

IncidentRoleTaskListDataItemType = Literal["incident_role_tasks"]

INCIDENT_ROLE_TASK_LIST_DATA_ITEM_TYPE_VALUES: set[IncidentRoleTaskListDataItemType] = {
    "incident_role_tasks",
}


def check_incident_role_task_list_data_item_type(value: str | None) -> IncidentRoleTaskListDataItemType | None:
    if value is None:
        return None
    if value in INCIDENT_ROLE_TASK_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(IncidentRoleTaskListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_ROLE_TASK_LIST_DATA_ITEM_TYPE_VALUES!r}")
