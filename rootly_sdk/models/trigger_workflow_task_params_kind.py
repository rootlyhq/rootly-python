from typing import Literal, cast

TriggerWorkflowTaskParamsKind = Literal["action_item", "alert", "incident", "post_mortem", "pulse"]

TRIGGER_WORKFLOW_TASK_PARAMS_KIND_VALUES: set[TriggerWorkflowTaskParamsKind] = {
    "action_item",
    "alert",
    "incident",
    "post_mortem",
    "pulse",
}


def check_trigger_workflow_task_params_kind(value: str | None) -> TriggerWorkflowTaskParamsKind | None:
    if value is None:
        return None
    if value in TRIGGER_WORKFLOW_TASK_PARAMS_KIND_VALUES:
        return cast(TriggerWorkflowTaskParamsKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRIGGER_WORKFLOW_TASK_PARAMS_KIND_VALUES!r}")
