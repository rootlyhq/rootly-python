from typing import Literal, cast

UpdateWorkflowCustomFieldSelectionDataType = Literal["workflow_custom_field_selections"]

UPDATE_WORKFLOW_CUSTOM_FIELD_SELECTION_DATA_TYPE_VALUES: set[UpdateWorkflowCustomFieldSelectionDataType] = {
    "workflow_custom_field_selections",
}


def check_update_workflow_custom_field_selection_data_type(value: str | None) -> UpdateWorkflowCustomFieldSelectionDataType | None:
    if value is None:
        return None
    if value in UPDATE_WORKFLOW_CUSTOM_FIELD_SELECTION_DATA_TYPE_VALUES:
        return cast(UpdateWorkflowCustomFieldSelectionDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_WORKFLOW_CUSTOM_FIELD_SELECTION_DATA_TYPE_VALUES!r}"
    )
