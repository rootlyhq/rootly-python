from typing import Literal, cast

WorkflowCustomFieldSelectionListDataItemType = Literal["workflow_custom_field_selections"]

WORKFLOW_CUSTOM_FIELD_SELECTION_LIST_DATA_ITEM_TYPE_VALUES: set[WorkflowCustomFieldSelectionListDataItemType] = {
    "workflow_custom_field_selections",
}


def check_workflow_custom_field_selection_list_data_item_type(
    value: str | None,
) -> WorkflowCustomFieldSelectionListDataItemType | None:
    if value is None:
        return None
    if value in WORKFLOW_CUSTOM_FIELD_SELECTION_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(WorkflowCustomFieldSelectionListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKFLOW_CUSTOM_FIELD_SELECTION_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
