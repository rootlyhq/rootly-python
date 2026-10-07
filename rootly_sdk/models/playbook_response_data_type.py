from typing import Literal

PlaybookResponseDataType = Literal["playbooks"]

PLAYBOOK_RESPONSE_DATA_TYPE_VALUES: set[PlaybookResponseDataType] = {
    "playbooks",
}


def check_playbook_response_data_type(value: str | None) -> PlaybookResponseDataType | None:
    if value is None:
        return None
    if value in PLAYBOOK_RESPONSE_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PLAYBOOK_RESPONSE_DATA_TYPE_VALUES!r}")
