from typing import Literal, cast

NewWorkflowCustomFieldSelectionDataType = Literal["workflow_custom_field_selections"]

NEW_WORKFLOW_CUSTOM_FIELD_SELECTION_DATA_TYPE_VALUES: set[NewWorkflowCustomFieldSelectionDataType] = {
    "workflow_custom_field_selections",
}


def check_new_workflow_custom_field_selection_data_type(
    value: str | None,
) -> NewWorkflowCustomFieldSelectionDataType | None:
    if value is None:
        return None
    if value in NEW_WORKFLOW_CUSTOM_FIELD_SELECTION_DATA_TYPE_VALUES:
        return cast(NewWorkflowCustomFieldSelectionDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_WORKFLOW_CUSTOM_FIELD_SELECTION_DATA_TYPE_VALUES!r}"
    )
