from typing import Literal, cast

NewPlaybookDataType = Literal["playbooks"]

NEW_PLAYBOOK_DATA_TYPE_VALUES: set[NewPlaybookDataType] = {
    "playbooks",
}


def check_new_playbook_data_type(value: str | None) -> NewPlaybookDataType | None:
    if value is None:
        return None
    if value in NEW_PLAYBOOK_DATA_TYPE_VALUES:
        return cast(NewPlaybookDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_PLAYBOOK_DATA_TYPE_VALUES!r}")
