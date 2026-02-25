from typing import Literal, cast

ListRetrospectiveProcessesInclude = Literal["groups", "incident_types", "retrospective_steps", "severities"]

LIST_RETROSPECTIVE_PROCESSES_INCLUDE_VALUES: set[ListRetrospectiveProcessesInclude] = {
    "groups",
    "incident_types",
    "retrospective_steps",
    "severities",
}


def check_list_retrospective_processes_include(value: str | None) -> ListRetrospectiveProcessesInclude | None:
    if value is None:
        return None
    if value in LIST_RETROSPECTIVE_PROCESSES_INCLUDE_VALUES:
        return cast(ListRetrospectiveProcessesInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_RETROSPECTIVE_PROCESSES_INCLUDE_VALUES!r}")
