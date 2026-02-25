from typing import Literal, cast

PlaybookTaskListDataItemType = Literal["playbook_tasks"]

PLAYBOOK_TASK_LIST_DATA_ITEM_TYPE_VALUES: set[PlaybookTaskListDataItemType] = {
    "playbook_tasks",
}


def check_playbook_task_list_data_item_type(value: str | None) -> PlaybookTaskListDataItemType | None:
    if value is None:
        return None
    if value in PLAYBOOK_TASK_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(PlaybookTaskListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PLAYBOOK_TASK_LIST_DATA_ITEM_TYPE_VALUES!r}")
