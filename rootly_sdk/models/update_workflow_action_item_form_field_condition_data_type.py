from typing import Literal, cast

UpdateWorkflowActionItemFormFieldConditionDataType = Literal["workflow_action_item_form_field_conditions"]

UPDATE_WORKFLOW_ACTION_ITEM_FORM_FIELD_CONDITION_DATA_TYPE_VALUES: set[
    UpdateWorkflowActionItemFormFieldConditionDataType
] = {
    "workflow_action_item_form_field_conditions",
}


def check_update_workflow_action_item_form_field_condition_data_type(
    value: str | None,
) -> UpdateWorkflowActionItemFormFieldConditionDataType | None:
    if value is None:
        return None
    if value in UPDATE_WORKFLOW_ACTION_ITEM_FORM_FIELD_CONDITION_DATA_TYPE_VALUES:
        return cast(UpdateWorkflowActionItemFormFieldConditionDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_WORKFLOW_ACTION_ITEM_FORM_FIELD_CONDITION_DATA_TYPE_VALUES!r}"
    )
