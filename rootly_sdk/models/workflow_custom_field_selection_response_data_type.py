from typing import Literal, cast

WorkflowCustomFieldSelectionResponseDataType = Literal["workflow_custom_field_selections"]

WORKFLOW_CUSTOM_FIELD_SELECTION_RESPONSE_DATA_TYPE_VALUES: set[WorkflowCustomFieldSelectionResponseDataType] = {
    "workflow_custom_field_selections",
}


def check_workflow_custom_field_selection_response_data_type(
    value: str | None,
) -> WorkflowCustomFieldSelectionResponseDataType | None:
    if value is None:
        return None
    if value in WORKFLOW_CUSTOM_FIELD_SELECTION_RESPONSE_DATA_TYPE_VALUES:
        return cast(WorkflowCustomFieldSelectionResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKFLOW_CUSTOM_FIELD_SELECTION_RESPONSE_DATA_TYPE_VALUES!r}"
    )
