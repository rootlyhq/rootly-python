from typing import Literal, cast

NewWorkflowDataType = Literal["workflows"]

NEW_WORKFLOW_DATA_TYPE_VALUES: set[NewWorkflowDataType] = {
    "workflows",
}


def check_new_workflow_data_type(value: str | None) -> NewWorkflowDataType | None:
    if value is None:
        return None
    if value in NEW_WORKFLOW_DATA_TYPE_VALUES:
        return cast(NewWorkflowDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_WORKFLOW_DATA_TYPE_VALUES!r}")
