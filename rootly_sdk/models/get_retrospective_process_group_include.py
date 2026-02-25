from typing import Literal, cast

GetRetrospectiveProcessGroupInclude = Literal["retrospective_process_group_steps"]

GET_RETROSPECTIVE_PROCESS_GROUP_INCLUDE_VALUES: set[GetRetrospectiveProcessGroupInclude] = {
    "retrospective_process_group_steps",
}


def check_get_retrospective_process_group_include(value: str | None) -> GetRetrospectiveProcessGroupInclude | None:
    if value is None:
        return None
    if value in GET_RETROSPECTIVE_PROCESS_GROUP_INCLUDE_VALUES:
        return cast(GetRetrospectiveProcessGroupInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_RETROSPECTIVE_PROCESS_GROUP_INCLUDE_VALUES!r}")
