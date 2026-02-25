from typing import Literal, cast

WorkflowRunResponseDataType = Literal["workflow_runs"]

WORKFLOW_RUN_RESPONSE_DATA_TYPE_VALUES: set[WorkflowRunResponseDataType] = {
    "workflow_runs",
}


def check_workflow_run_response_data_type(value: str | None) -> WorkflowRunResponseDataType | None:
    if value is None:
        return None
    if value in WORKFLOW_RUN_RESPONSE_DATA_TYPE_VALUES:
        return cast(WorkflowRunResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKFLOW_RUN_RESPONSE_DATA_TYPE_VALUES!r}")
