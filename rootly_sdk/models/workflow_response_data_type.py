from typing import Literal, cast

WorkflowResponseDataType = Literal["workflows"]

WORKFLOW_RESPONSE_DATA_TYPE_VALUES: set[WorkflowResponseDataType] = {
    "workflows",
}


def check_workflow_response_data_type(value: str | None) -> WorkflowResponseDataType | None:
    if value is None:
        return None
    if value in WORKFLOW_RESPONSE_DATA_TYPE_VALUES:
        return cast(WorkflowResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKFLOW_RESPONSE_DATA_TYPE_VALUES!r}")
