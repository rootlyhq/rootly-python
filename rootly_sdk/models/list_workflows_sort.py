from typing import Literal, cast

ListWorkflowsSort = Literal["-created_at", "-position", "-updated_at", "created_at", "position", "updated_at"]

LIST_WORKFLOWS_SORT_VALUES: set[ListWorkflowsSort] = {
    "-created_at",
    "-position",
    "-updated_at",
    "created_at",
    "position",
    "updated_at",
}


def check_list_workflows_sort(value: str | None) -> ListWorkflowsSort | None:
    if value is None:
        return None
    if value in LIST_WORKFLOWS_SORT_VALUES:
        return cast(ListWorkflowsSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_WORKFLOWS_SORT_VALUES!r}")
