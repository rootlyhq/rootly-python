from typing import Literal, cast

NewWorkflowDataAttributesPriority = Literal["high", "low", "normal"]

NEW_WORKFLOW_DATA_ATTRIBUTES_PRIORITY_VALUES: set[NewWorkflowDataAttributesPriority] = {
    "high",
    "low",
    "normal",
}


def check_new_workflow_data_attributes_priority(value: str | None) -> NewWorkflowDataAttributesPriority | None:
    if value is None:
        return None
    if value in NEW_WORKFLOW_DATA_ATTRIBUTES_PRIORITY_VALUES:
        return cast(NewWorkflowDataAttributesPriority, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_WORKFLOW_DATA_ATTRIBUTES_PRIORITY_VALUES!r}")
