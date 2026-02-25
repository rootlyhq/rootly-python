from typing import Literal, cast

ShiftListDataItemType = Literal["shifts"]

SHIFT_LIST_DATA_ITEM_TYPE_VALUES: set[ShiftListDataItemType] = {
    "shifts",
}


def check_shift_list_data_item_type(value: str | None) -> ShiftListDataItemType | None:
    if value is None:
        return None
    if value in SHIFT_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(ShiftListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SHIFT_LIST_DATA_ITEM_TYPE_VALUES!r}")
