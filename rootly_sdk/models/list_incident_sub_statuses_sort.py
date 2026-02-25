from typing import Literal, cast

ListIncidentSubStatusesSort = Literal[
    "-assigned_at", "-created_at", "-updated_at", "assigned_at", "created_at", "updated_at"
]

LIST_INCIDENT_SUB_STATUSES_SORT_VALUES: set[ListIncidentSubStatusesSort] = {
    "-assigned_at",
    "-created_at",
    "-updated_at",
    "assigned_at",
    "created_at",
    "updated_at",
}


def check_list_incident_sub_statuses_sort(value: str | None) -> ListIncidentSubStatusesSort | None:
    if value is None:
        return None
    if value in LIST_INCIDENT_SUB_STATUSES_SORT_VALUES:
        return cast(ListIncidentSubStatusesSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INCIDENT_SUB_STATUSES_SORT_VALUES!r}")
