from typing import Literal, cast

ListWorkflowRunsInclude = Literal["genius_task_runs"]

LIST_WORKFLOW_RUNS_INCLUDE_VALUES: set[ListWorkflowRunsInclude] = {
    "genius_task_runs",
}


def check_list_workflow_runs_include(value: str | None) -> ListWorkflowRunsInclude | None:
    if value is None:
        return None
    if value in LIST_WORKFLOW_RUNS_INCLUDE_VALUES:
        return cast(ListWorkflowRunsInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_WORKFLOW_RUNS_INCLUDE_VALUES!r}")
