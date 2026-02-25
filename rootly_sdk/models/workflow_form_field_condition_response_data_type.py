from typing import Literal, cast

WorkflowFormFieldConditionResponseDataType = Literal["workflow_form_field_conditions"]

WORKFLOW_FORM_FIELD_CONDITION_RESPONSE_DATA_TYPE_VALUES: set[WorkflowFormFieldConditionResponseDataType] = {
    "workflow_form_field_conditions",
}


def check_workflow_form_field_condition_response_data_type(value: str | None) -> WorkflowFormFieldConditionResponseDataType | None:
    if value is None:
        return None
    if value in WORKFLOW_FORM_FIELD_CONDITION_RESPONSE_DATA_TYPE_VALUES:
        return cast(WorkflowFormFieldConditionResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKFLOW_FORM_FIELD_CONDITION_RESPONSE_DATA_TYPE_VALUES!r}"
    )
