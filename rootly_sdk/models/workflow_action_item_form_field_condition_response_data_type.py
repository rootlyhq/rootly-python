from typing import Literal, cast

WorkflowActionItemFormFieldConditionResponseDataType = Literal["workflow_action_item_form_field_conditions"]

WORKFLOW_ACTION_ITEM_FORM_FIELD_CONDITION_RESPONSE_DATA_TYPE_VALUES: set[
    WorkflowActionItemFormFieldConditionResponseDataType
] = {
    "workflow_action_item_form_field_conditions",
}


def check_workflow_action_item_form_field_condition_response_data_type(
    value: str | None,
) -> WorkflowActionItemFormFieldConditionResponseDataType | None:
    if value is None:
        return None
    if value in WORKFLOW_ACTION_ITEM_FORM_FIELD_CONDITION_RESPONSE_DATA_TYPE_VALUES:
        return cast(WorkflowActionItemFormFieldConditionResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKFLOW_ACTION_ITEM_FORM_FIELD_CONDITION_RESPONSE_DATA_TYPE_VALUES!r}"
    )
