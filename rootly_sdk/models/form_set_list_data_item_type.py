from typing import Literal, cast

FormSetListDataItemType = Literal["form_sets"]

FORM_SET_LIST_DATA_ITEM_TYPE_VALUES: set[FormSetListDataItemType] = {
    "form_sets",
}


def check_form_set_list_data_item_type(value: str | None) -> FormSetListDataItemType | None:
    if value is None:
        return None
    if value in FORM_SET_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(FormSetListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORM_SET_LIST_DATA_ITEM_TYPE_VALUES!r}")
