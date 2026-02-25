from typing import Literal, cast

UpdateWorkflowFormFieldConditionDataType = Literal["workflow_form_field_conditions"]

UPDATE_WORKFLOW_FORM_FIELD_CONDITION_DATA_TYPE_VALUES: set[UpdateWorkflowFormFieldConditionDataType] = {
    "workflow_form_field_conditions",
}


def check_update_workflow_form_field_condition_data_type(value: str | None) -> UpdateWorkflowFormFieldConditionDataType | None:
    if value is None:
        return None
    if value in UPDATE_WORKFLOW_FORM_FIELD_CONDITION_DATA_TYPE_VALUES:
        return cast(UpdateWorkflowFormFieldConditionDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_WORKFLOW_FORM_FIELD_CONDITION_DATA_TYPE_VALUES!r}"
    )
