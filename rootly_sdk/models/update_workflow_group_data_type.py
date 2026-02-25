from typing import Literal, cast

UpdateWorkflowGroupDataType = Literal["workflow_groups"]

UPDATE_WORKFLOW_GROUP_DATA_TYPE_VALUES: set[UpdateWorkflowGroupDataType] = {
    "workflow_groups",
}


def check_update_workflow_group_data_type(value: str | None) -> UpdateWorkflowGroupDataType | None:
    if value is None:
        return None
    if value in UPDATE_WORKFLOW_GROUP_DATA_TYPE_VALUES:
        return cast(UpdateWorkflowGroupDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_WORKFLOW_GROUP_DATA_TYPE_VALUES!r}")
