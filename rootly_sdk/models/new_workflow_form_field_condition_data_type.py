from typing import Literal, cast

NewWorkflowFormFieldConditionDataType = Literal["workflow_form_field_conditions"]

NEW_WORKFLOW_FORM_FIELD_CONDITION_DATA_TYPE_VALUES: set[NewWorkflowFormFieldConditionDataType] = {
    "workflow_form_field_conditions",
}


def check_new_workflow_form_field_condition_data_type(
    value: str | None,
) -> NewWorkflowFormFieldConditionDataType | None:
    if value is None:
        return None
    if value in NEW_WORKFLOW_FORM_FIELD_CONDITION_DATA_TYPE_VALUES:
        return cast(NewWorkflowFormFieldConditionDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_WORKFLOW_FORM_FIELD_CONDITION_DATA_TYPE_VALUES!r}"
    )
