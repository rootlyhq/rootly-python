from typing import Literal, cast

TriggerWorkflowTaskParamsTaskType = Literal["trigger_workflow"]

TRIGGER_WORKFLOW_TASK_PARAMS_TASK_TYPE_VALUES: set[TriggerWorkflowTaskParamsTaskType] = {
    "trigger_workflow",
}


def check_trigger_workflow_task_params_task_type(value: str | None) -> TriggerWorkflowTaskParamsTaskType | None:
    if value is None:
        return None
    if value in TRIGGER_WORKFLOW_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(TriggerWorkflowTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRIGGER_WORKFLOW_TASK_PARAMS_TASK_TYPE_VALUES!r}")
