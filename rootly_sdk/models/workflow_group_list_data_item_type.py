from typing import Literal, cast

WorkflowGroupListDataItemType = Literal["workflow_groups"]

WORKFLOW_GROUP_LIST_DATA_ITEM_TYPE_VALUES: set[WorkflowGroupListDataItemType] = {
    "workflow_groups",
}


def check_workflow_group_list_data_item_type(value: str | None) -> WorkflowGroupListDataItemType | None:
    if value is None:
        return None
    if value in WORKFLOW_GROUP_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(WorkflowGroupListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKFLOW_GROUP_LIST_DATA_ITEM_TYPE_VALUES!r}")
