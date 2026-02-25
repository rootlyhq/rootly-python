from typing import Literal, cast

ListRetrospectiveProcessGroupsSort = Literal[
    "-created_at", "-position", "-updated_at", "created_at", "position", "updated_at"
]

LIST_RETROSPECTIVE_PROCESS_GROUPS_SORT_VALUES: set[ListRetrospectiveProcessGroupsSort] = {
    "-created_at",
    "-position",
    "-updated_at",
    "created_at",
    "position",
    "updated_at",
}


def check_list_retrospective_process_groups_sort(value: str | None) -> ListRetrospectiveProcessGroupsSort | None:
    if value is None:
        return None
    if value in LIST_RETROSPECTIVE_PROCESS_GROUPS_SORT_VALUES:
        return cast(ListRetrospectiveProcessGroupsSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_RETROSPECTIVE_PROCESS_GROUPS_SORT_VALUES!r}")
