from typing import Literal, cast

WorkflowActionItemFormFieldConditionListDataItemType = Literal["workflow_action_item_form_field_conditions"]

WORKFLOW_ACTION_ITEM_FORM_FIELD_CONDITION_LIST_DATA_ITEM_TYPE_VALUES: set[
    WorkflowActionItemFormFieldConditionListDataItemType
] = {
    "workflow_action_item_form_field_conditions",
}


def check_workflow_action_item_form_field_condition_list_data_item_type(
    value: str | None,
) -> WorkflowActionItemFormFieldConditionListDataItemType | None:
    if value is None:
        return None
    if value in WORKFLOW_ACTION_ITEM_FORM_FIELD_CONDITION_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(WorkflowActionItemFormFieldConditionListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKFLOW_ACTION_ITEM_FORM_FIELD_CONDITION_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
