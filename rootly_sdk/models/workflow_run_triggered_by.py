from typing import Literal, cast

WorkflowRunTriggeredBy = Literal["system", "user", "workflow"]

WORKFLOW_RUN_TRIGGERED_BY_VALUES: set[WorkflowRunTriggeredBy] = {
    "system",
    "user",
    "workflow",
}


def check_workflow_run_triggered_by(value: str | None) -> WorkflowRunTriggeredBy | None:
    if value is None:
        return None
    if value in WORKFLOW_RUN_TRIGGERED_BY_VALUES:
        return cast(WorkflowRunTriggeredBy, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKFLOW_RUN_TRIGGERED_BY_VALUES!r}")
