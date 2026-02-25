from typing import Literal, cast

CustomFieldOptionListDataItemType = Literal["custom_field_options"]

CUSTOM_FIELD_OPTION_LIST_DATA_ITEM_TYPE_VALUES: set[CustomFieldOptionListDataItemType] = {
    "custom_field_options",
}


def check_custom_field_option_list_data_item_type(value: str | None) -> CustomFieldOptionListDataItemType | None:
    if value is None:
        return None
    if value in CUSTOM_FIELD_OPTION_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(CustomFieldOptionListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELD_OPTION_LIST_DATA_ITEM_TYPE_VALUES!r}")
