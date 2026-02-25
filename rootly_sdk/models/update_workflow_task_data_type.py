from typing import Literal, cast

UpdateWorkflowTaskDataType = Literal["workflow_tasks"]

UPDATE_WORKFLOW_TASK_DATA_TYPE_VALUES: set[UpdateWorkflowTaskDataType] = {
    "workflow_tasks",
}


def check_update_workflow_task_data_type(value: str | None) -> UpdateWorkflowTaskDataType | None:
    if value is None:
        return None
    if value in UPDATE_WORKFLOW_TASK_DATA_TYPE_VALUES:
        return cast(UpdateWorkflowTaskDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_WORKFLOW_TASK_DATA_TYPE_VALUES!r}")
