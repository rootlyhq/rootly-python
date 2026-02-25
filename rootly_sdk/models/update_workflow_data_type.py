from typing import Literal, cast

UpdateWorkflowDataType = Literal["workflows"]

UPDATE_WORKFLOW_DATA_TYPE_VALUES: set[UpdateWorkflowDataType] = {
    "workflows",
}


def check_update_workflow_data_type(value: str | None) -> UpdateWorkflowDataType | None:
    if value is None:
        return None
    if value in UPDATE_WORKFLOW_DATA_TYPE_VALUES:
        return cast(UpdateWorkflowDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_WORKFLOW_DATA_TYPE_VALUES!r}")
