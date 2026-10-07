from typing import Literal

PlaybookTaskResponseDataType = Literal["playbook_tasks"]

PLAYBOOK_TASK_RESPONSE_DATA_TYPE_VALUES: set[PlaybookTaskResponseDataType] = {
    "playbook_tasks",
}


def check_playbook_task_response_data_type(value: str | None) -> PlaybookTaskResponseDataType | None:
    if value is None:
        return None
    if value in PLAYBOOK_TASK_RESPONSE_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PLAYBOOK_TASK_RESPONSE_DATA_TYPE_VALUES!r}")
