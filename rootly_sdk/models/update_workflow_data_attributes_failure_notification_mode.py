from typing import Literal

UpdateWorkflowDataAttributesFailureNotificationMode = Literal["custom", "inherit", "off"]

UPDATE_WORKFLOW_DATA_ATTRIBUTES_FAILURE_NOTIFICATION_MODE_VALUES: set[
    UpdateWorkflowDataAttributesFailureNotificationMode
] = {
    "custom",
    "inherit",
    "off",
}


def check_update_workflow_data_attributes_failure_notification_mode(
    value: str | None,
) -> UpdateWorkflowDataAttributesFailureNotificationMode | None:
    if value is None:
        return None
    if value in UPDATE_WORKFLOW_DATA_ATTRIBUTES_FAILURE_NOTIFICATION_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_WORKFLOW_DATA_ATTRIBUTES_FAILURE_NOTIFICATION_MODE_VALUES!r}"
    )
