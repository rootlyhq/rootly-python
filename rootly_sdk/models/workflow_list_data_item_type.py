from typing import Literal, cast

WorkflowListDataItemType = Literal["workflows"]

WORKFLOW_LIST_DATA_ITEM_TYPE_VALUES: set[WorkflowListDataItemType] = {
    "workflows",
}


def check_workflow_list_data_item_type(value: str | None) -> WorkflowListDataItemType | None:
    if value is None:
        return None
    if value in WORKFLOW_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(WorkflowListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKFLOW_LIST_DATA_ITEM_TYPE_VALUES!r}")
