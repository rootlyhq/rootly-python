from typing import Literal, cast

NewWorkflowActionItemFormFieldConditionDataAttributesActionItemCondition = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

NEW_WORKFLOW_ACTION_ITEM_FORM_FIELD_CONDITION_DATA_ATTRIBUTES_ACTION_ITEM_CONDITION_VALUES: set[
    NewWorkflowActionItemFormFieldConditionDataAttributesActionItemCondition
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


def check_new_workflow_action_item_form_field_condition_data_attributes_action_item_condition(
    value: str | None,
) -> NewWorkflowActionItemFormFieldConditionDataAttributesActionItemCondition | None:
    if value is None:
        return None
    if value in NEW_WORKFLOW_ACTION_ITEM_FORM_FIELD_CONDITION_DATA_ATTRIBUTES_ACTION_ITEM_CONDITION_VALUES:
        return cast(NewWorkflowActionItemFormFieldConditionDataAttributesActionItemCondition, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_WORKFLOW_ACTION_ITEM_FORM_FIELD_CONDITION_DATA_ATTRIBUTES_ACTION_ITEM_CONDITION_VALUES!r}"
    )
