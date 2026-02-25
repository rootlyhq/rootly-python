from typing import Literal, cast

ListRetrospectiveProcessGroupsInclude = Literal["retrospective_process_group_steps"]

LIST_RETROSPECTIVE_PROCESS_GROUPS_INCLUDE_VALUES: set[ListRetrospectiveProcessGroupsInclude] = {
    "retrospective_process_group_steps",
}


def check_list_retrospective_process_groups_include(value: str | None) -> ListRetrospectiveProcessGroupsInclude | None:
    if value is None:
        return None
    if value in LIST_RETROSPECTIVE_PROCESS_GROUPS_INCLUDE_VALUES:
        return cast(ListRetrospectiveProcessGroupsInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_RETROSPECTIVE_PROCESS_GROUPS_INCLUDE_VALUES!r}")
