from typing import Literal, cast

NewWorkflowGroupDataType = Literal["workflow_groups"]

NEW_WORKFLOW_GROUP_DATA_TYPE_VALUES: set[NewWorkflowGroupDataType] = {
    "workflow_groups",
}


def check_new_workflow_group_data_type(value: str | None) -> NewWorkflowGroupDataType | None:
    if value is None:
        return None
    if value in NEW_WORKFLOW_GROUP_DATA_TYPE_VALUES:
        return cast(NewWorkflowGroupDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_WORKFLOW_GROUP_DATA_TYPE_VALUES!r}")
