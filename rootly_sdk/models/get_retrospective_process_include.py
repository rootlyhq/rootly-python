from typing import Literal, cast

GetRetrospectiveProcessInclude = Literal["groups", "incident_types", "retrospective_steps", "severities"]

GET_RETROSPECTIVE_PROCESS_INCLUDE_VALUES: set[GetRetrospectiveProcessInclude] = {
    "groups",
    "incident_types",
    "retrospective_steps",
    "severities",
}


def check_get_retrospective_process_include(value: str | None) -> GetRetrospectiveProcessInclude | None:
    if value is None:
        return None
    if value in GET_RETROSPECTIVE_PROCESS_INCLUDE_VALUES:
        return cast(GetRetrospectiveProcessInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_RETROSPECTIVE_PROCESS_INCLUDE_VALUES!r}")
