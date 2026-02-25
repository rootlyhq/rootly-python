from typing import Literal, cast

WorkflowTaskResponseDataType = Literal["workflow_tasks"]

WORKFLOW_TASK_RESPONSE_DATA_TYPE_VALUES: set[WorkflowTaskResponseDataType] = {
    "workflow_tasks",
}


def check_workflow_task_response_data_type(value: str | None) -> WorkflowTaskResponseDataType | None:
    if value is None:
        return None
    if value in WORKFLOW_TASK_RESPONSE_DATA_TYPE_VALUES:
        return cast(WorkflowTaskResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKFLOW_TASK_RESPONSE_DATA_TYPE_VALUES!r}")
