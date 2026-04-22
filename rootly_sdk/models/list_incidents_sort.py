from typing import Literal, cast

ListIncidentsSort = Literal[
    "-created_at",
    "-in_triage_at",
    "-mitigated_at",
    "-resolved_at",
    "-started_at",
    "-updated_at",
    "created_at",
    "in_triage_at",
    "mitigated_at",
    "resolved_at",
    "started_at",
    "updated_at",
]

LIST_INCIDENTS_SORT_VALUES: set[ListIncidentsSort] = {
    "-created_at",
    "-in_triage_at",
    "-mitigated_at",
    "-resolved_at",
    "-started_at",
    "-updated_at",
    "created_at",
    "in_triage_at",
    "mitigated_at",
    "resolved_at",
    "started_at",
    "updated_at",
}


def check_list_incidents_sort(value: str | None) -> ListIncidentsSort | None:
    if value is None:
        return None
    if value in LIST_INCIDENTS_SORT_VALUES:
        return cast(ListIncidentsSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INCIDENTS_SORT_VALUES!r}")
