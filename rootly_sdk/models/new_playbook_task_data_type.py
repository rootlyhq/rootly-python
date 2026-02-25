from typing import Literal, cast

NewPlaybookTaskDataType = Literal["playbook_tasks"]

NEW_PLAYBOOK_TASK_DATA_TYPE_VALUES: set[NewPlaybookTaskDataType] = {
    "playbook_tasks",
}


def check_new_playbook_task_data_type(value: str | None) -> NewPlaybookTaskDataType | None:
    if value is None:
        return None
    if value in NEW_PLAYBOOK_TASK_DATA_TYPE_VALUES:
        return cast(NewPlaybookTaskDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_PLAYBOOK_TASK_DATA_TYPE_VALUES!r}")
