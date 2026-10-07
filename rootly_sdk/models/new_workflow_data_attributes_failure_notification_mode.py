from typing import Literal

NewWorkflowDataAttributesFailureNotificationMode = Literal["custom", "inherit", "off"]

NEW_WORKFLOW_DATA_ATTRIBUTES_FAILURE_NOTIFICATION_MODE_VALUES: set[NewWorkflowDataAttributesFailureNotificationMode] = {
    "custom",
    "inherit",
    "off",
}


def check_new_workflow_data_attributes_failure_notification_mode(
    value: str | None,
) -> NewWorkflowDataAttributesFailureNotificationMode | None:
    if value is None:
        return None
    if value in NEW_WORKFLOW_DATA_ATTRIBUTES_FAILURE_NOTIFICATION_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_WORKFLOW_DATA_ATTRIBUTES_FAILURE_NOTIFICATION_MODE_VALUES!r}"
    )
