from typing import Literal, cast

OverrideShiftListDataItemType = Literal["shifts"]

OVERRIDE_SHIFT_LIST_DATA_ITEM_TYPE_VALUES: set[OverrideShiftListDataItemType] = {
    "shifts",
}


def check_override_shift_list_data_item_type(value: str | None) -> OverrideShiftListDataItemType | None:
    if value is None:
        return None
    if value in OVERRIDE_SHIFT_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(OverrideShiftListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OVERRIDE_SHIFT_LIST_DATA_ITEM_TYPE_VALUES!r}")
