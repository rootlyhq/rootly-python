from typing import Literal, cast

UpdatePlaybookTaskDataType = Literal["playbook_tasks"]

UPDATE_PLAYBOOK_TASK_DATA_TYPE_VALUES: set[UpdatePlaybookTaskDataType] = {
    "playbook_tasks",
}


def check_update_playbook_task_data_type(value: str | None) -> UpdatePlaybookTaskDataType | None:
    if value is None:
        return None
    if value in UPDATE_PLAYBOOK_TASK_DATA_TYPE_VALUES:
        return cast(UpdatePlaybookTaskDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_PLAYBOOK_TASK_DATA_TYPE_VALUES!r}")
