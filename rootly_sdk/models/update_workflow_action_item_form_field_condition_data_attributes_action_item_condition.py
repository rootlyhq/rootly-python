from typing import Literal

UpdateWorkflowActionItemFormFieldConditionDataAttributesActionItemCondition = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

UPDATE_WORKFLOW_ACTION_ITEM_FORM_FIELD_CONDITION_DATA_ATTRIBUTES_ACTION_ITEM_CONDITION_VALUES: set[
    UpdateWorkflowActionItemFormFieldConditionDataAttributesActionItemCondition
] = {
    "ANY",
    "CONTAINS",
    "CONTAINS_ALL",
    "CONTAINS_NONE",
    "IS",
    "IS NOT",
    "NONE",
    "SET",
    "UNSET",
}


def check_update_workflow_action_item_form_field_condition_data_attributes_action_item_condition(
    value: str | None,
) -> UpdateWorkflowActionItemFormFieldConditionDataAttributesActionItemCondition | None:
    if value is None:
        return None
    if value in UPDATE_WORKFLOW_ACTION_ITEM_FORM_FIELD_CONDITION_DATA_ATTRIBUTES_ACTION_ITEM_CONDITION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_WORKFLOW_ACTION_ITEM_FORM_FIELD_CONDITION_DATA_ATTRIBUTES_ACTION_ITEM_CONDITION_VALUES!r}"
    )
