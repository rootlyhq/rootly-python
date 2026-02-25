from typing import Literal, cast

WorkflowFormFieldConditionListDataItemType = Literal["workflow_form_field_conditions"]

WORKFLOW_FORM_FIELD_CONDITION_LIST_DATA_ITEM_TYPE_VALUES: set[WorkflowFormFieldConditionListDataItemType] = {
    "workflow_form_field_conditions",
}


def check_workflow_form_field_condition_list_data_item_type(
    value: str | None,
) -> WorkflowFormFieldConditionListDataItemType | None:
    if value is None:
        return None
    if value in WORKFLOW_FORM_FIELD_CONDITION_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(WorkflowFormFieldConditionListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKFLOW_FORM_FIELD_CONDITION_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
