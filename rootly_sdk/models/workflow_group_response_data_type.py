from typing import Literal, cast

WorkflowGroupResponseDataType = Literal["workflow_groups"]

WORKFLOW_GROUP_RESPONSE_DATA_TYPE_VALUES: set[WorkflowGroupResponseDataType] = {
    "workflow_groups",
}


def check_workflow_group_response_data_type(value: str | None) -> WorkflowGroupResponseDataType | None:
    if value is None:
        return None
    if value in WORKFLOW_GROUP_RESPONSE_DATA_TYPE_VALUES:
        return cast(WorkflowGroupResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKFLOW_GROUP_RESPONSE_DATA_TYPE_VALUES!r}")
