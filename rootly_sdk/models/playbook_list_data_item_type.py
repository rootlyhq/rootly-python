from typing import Literal, cast

PlaybookListDataItemType = Literal["playbooks"]

PLAYBOOK_LIST_DATA_ITEM_TYPE_VALUES: set[PlaybookListDataItemType] = {
    "playbooks",
}


def check_playbook_list_data_item_type(value: str | None) -> PlaybookListDataItemType | None:
    if value is None:
        return None
    if value in PLAYBOOK_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(PlaybookListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PLAYBOOK_LIST_DATA_ITEM_TYPE_VALUES!r}")
