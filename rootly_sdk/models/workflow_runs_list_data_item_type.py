from typing import Literal, cast

WorkflowRunsListDataItemType = Literal["workflow_runs"]

WORKFLOW_RUNS_LIST_DATA_ITEM_TYPE_VALUES: set[WorkflowRunsListDataItemType] = {
    "workflow_runs",
}


def check_workflow_runs_list_data_item_type(value: str | None) -> WorkflowRunsListDataItemType | None:
    if value is None:
        return None
    if value in WORKFLOW_RUNS_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(WorkflowRunsListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKFLOW_RUNS_LIST_DATA_ITEM_TYPE_VALUES!r}")
