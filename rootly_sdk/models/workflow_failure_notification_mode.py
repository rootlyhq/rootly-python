from typing import Literal

WorkflowFailureNotificationMode = Literal["custom", "inherit", "off"]

WORKFLOW_FAILURE_NOTIFICATION_MODE_VALUES: set[WorkflowFailureNotificationMode] = {
    "custom",
    "inherit",
    "off",
}


def check_workflow_failure_notification_mode(value: str | None) -> WorkflowFailureNotificationMode | None:
    if value is None:
        return None
    if value in WORKFLOW_FAILURE_NOTIFICATION_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKFLOW_FAILURE_NOTIFICATION_MODE_VALUES!r}")
