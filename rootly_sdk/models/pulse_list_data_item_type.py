from typing import Literal, cast

PulseListDataItemType = Literal["pulses"]

PULSE_LIST_DATA_ITEM_TYPE_VALUES: set[PulseListDataItemType] = {
    "pulses",
}


def check_pulse_list_data_item_type(value: str | None) -> PulseListDataItemType | None:
    if value is None:
        return None
    if value in PULSE_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(PulseListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PULSE_LIST_DATA_ITEM_TYPE_VALUES!r}")
