from typing import Literal, cast

WorkflowRunStatus = Literal["canceled", "completed", "completed_with_errors", "failed", "queued", "started"]

WORKFLOW_RUN_STATUS_VALUES: set[WorkflowRunStatus] = {
    "canceled",
    "completed",
    "completed_with_errors",
    "failed",
    "queued",
    "started",
}


def check_workflow_run_status(value: str | None) -> WorkflowRunStatus | None:
    if value is None:
        return None
    if value in WORKFLOW_RUN_STATUS_VALUES:
        return cast(WorkflowRunStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKFLOW_RUN_STATUS_VALUES!r}")
