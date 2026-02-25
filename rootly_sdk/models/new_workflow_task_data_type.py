from typing import Literal, cast

NewWorkflowTaskDataType = Literal["workflow_tasks"]

NEW_WORKFLOW_TASK_DATA_TYPE_VALUES: set[NewWorkflowTaskDataType] = {
    "workflow_tasks",
}


def check_new_workflow_task_data_type(value: str | None) -> NewWorkflowTaskDataType | None:
    if value is None:
        return None
    if value in NEW_WORKFLOW_TASK_DATA_TYPE_VALUES:
        return cast(NewWorkflowTaskDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_WORKFLOW_TASK_DATA_TYPE_VALUES!r}")
