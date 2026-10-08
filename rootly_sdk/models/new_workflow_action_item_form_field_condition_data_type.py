from typing import Literal

NewWorkflowActionItemFormFieldConditionDataType = Literal["workflow_action_item_form_field_conditions"]

NEW_WORKFLOW_ACTION_ITEM_FORM_FIELD_CONDITION_DATA_TYPE_VALUES: set[NewWorkflowActionItemFormFieldConditionDataType] = {
    "workflow_action_item_form_field_conditions",
}


def check_new_workflow_action_item_form_field_condition_data_type(
    value: str | None,
) -> NewWorkflowActionItemFormFieldConditionDataType | None:
    if value is None:
        return None
    if value in NEW_WORKFLOW_ACTION_ITEM_FORM_FIELD_CONDITION_DATA_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_WORKFLOW_ACTION_ITEM_FORM_FIELD_CONDITION_DATA_TYPE_VALUES!r}"
    )
