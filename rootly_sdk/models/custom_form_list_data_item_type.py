from typing import Literal, cast

CustomFormListDataItemType = Literal["custom_forms"]

CUSTOM_FORM_LIST_DATA_ITEM_TYPE_VALUES: set[CustomFormListDataItemType] = {
    "custom_forms",
}


def check_custom_form_list_data_item_type(value: str | None) -> CustomFormListDataItemType | None:
    if value is None:
        return None
    if value in CUSTOM_FORM_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(CustomFormListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOM_FORM_LIST_DATA_ITEM_TYPE_VALUES!r}")
