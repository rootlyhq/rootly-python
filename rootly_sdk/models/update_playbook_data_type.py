from typing import Literal, cast

UpdatePlaybookDataType = Literal["playbooks"]

UPDATE_PLAYBOOK_DATA_TYPE_VALUES: set[UpdatePlaybookDataType] = {
    "playbooks",
}


def check_update_playbook_data_type(value: str | None) -> UpdatePlaybookDataType | None:
    if value is None:
        return None
    if value in UPDATE_PLAYBOOK_DATA_TYPE_VALUES:
        return cast(UpdatePlaybookDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_PLAYBOOK_DATA_TYPE_VALUES!r}")
