from typing import Literal, cast

WorkflowActionItemFormFieldConditionActionItemCondition = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

WORKFLOW_ACTION_ITEM_FORM_FIELD_CONDITION_ACTION_ITEM_CONDITION_VALUES: set[
    WorkflowActionItemFormFieldConditionActionItemCondition
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


def check_workflow_action_item_form_field_condition_action_item_condition(
    value: str | None,
) -> WorkflowActionItemFormFieldConditionActionItemCondition | None:
    if value is None:
        return None
    if value in WORKFLOW_ACTION_ITEM_FORM_FIELD_CONDITION_ACTION_ITEM_CONDITION_VALUES:
        return cast(WorkflowActionItemFormFieldConditionActionItemCondition, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKFLOW_ACTION_ITEM_FORM_FIELD_CONDITION_ACTION_ITEM_CONDITION_VALUES!r}"
    )
