from typing import Literal, cast

RetrospectiveProcessListDataItemType = Literal["retrospective_processes"]

RETROSPECTIVE_PROCESS_LIST_DATA_ITEM_TYPE_VALUES: set[RetrospectiveProcessListDataItemType] = {
    "retrospective_processes",
}


def check_retrospective_process_list_data_item_type(value: str | None) -> RetrospectiveProcessListDataItemType | None:
    if value is None:
        return None
    if value in RETROSPECTIVE_PROCESS_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(RetrospectiveProcessListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RETROSPECTIVE_PROCESS_LIST_DATA_ITEM_TYPE_VALUES!r}")
