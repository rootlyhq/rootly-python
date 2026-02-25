from typing import Literal, cast

CauseListDataItemType = Literal["causes"]

CAUSE_LIST_DATA_ITEM_TYPE_VALUES: set[CauseListDataItemType] = {
    "causes",
}


def check_cause_list_data_item_type(value: str | None) -> CauseListDataItemType | None:
    if value is None:
        return None
    if value in CAUSE_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(CauseListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CAUSE_LIST_DATA_ITEM_TYPE_VALUES!r}")
