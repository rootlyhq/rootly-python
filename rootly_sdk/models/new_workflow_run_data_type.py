from typing import Literal, cast

NewWorkflowRunDataType = Literal["workflow_runs"]

NEW_WORKFLOW_RUN_DATA_TYPE_VALUES: set[NewWorkflowRunDataType] = {
    "workflow_runs",
}


def check_new_workflow_run_data_type(value: str | None) -> NewWorkflowRunDataType | None:
    if value is None:
        return None
    if value in NEW_WORKFLOW_RUN_DATA_TYPE_VALUES:
        return cast(NewWorkflowRunDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_WORKFLOW_RUN_DATA_TYPE_VALUES!r}")
