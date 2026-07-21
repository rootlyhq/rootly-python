from typing import Literal, cast

OncallListDataItemType = Literal["on_call_resources"]

ONCALL_LIST_DATA_ITEM_TYPE_VALUES: set[OncallListDataItemType] = {
    "on_call_resources",
}


def check_oncall_list_data_item_type(value: str | None) -> OncallListDataItemType | None:
    if value is None:
        return None
    if value in ONCALL_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(OncallListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ONCALL_LIST_DATA_ITEM_TYPE_VALUES!r}")
