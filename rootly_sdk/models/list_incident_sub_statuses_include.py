from typing import Literal, cast

ListIncidentSubStatusesInclude = Literal["assigned_by_user", "sub_status"]

LIST_INCIDENT_SUB_STATUSES_INCLUDE_VALUES: set[ListIncidentSubStatusesInclude] = {
    "assigned_by_user",
    "sub_status",
}


def check_list_incident_sub_statuses_include(value: str | None) -> ListIncidentSubStatusesInclude | None:
    if value is None:
        return None
    if value in LIST_INCIDENT_SUB_STATUSES_INCLUDE_VALUES:
        return cast(ListIncidentSubStatusesInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INCIDENT_SUB_STATUSES_INCLUDE_VALUES!r}")
