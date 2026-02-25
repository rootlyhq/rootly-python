from typing import Literal, cast

CustomFieldListDataItemType = Literal["custom_fields"]

CUSTOM_FIELD_LIST_DATA_ITEM_TYPE_VALUES: set[CustomFieldListDataItemType] = {
    "custom_fields",
}


def check_custom_field_list_data_item_type(value: str | None) -> CustomFieldListDataItemType | None:
    if value is None:
        return None
    if value in CUSTOM_FIELD_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(CustomFieldListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELD_LIST_DATA_ITEM_TYPE_VALUES!r}")
