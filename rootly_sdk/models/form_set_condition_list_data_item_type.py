from typing import Literal

FormSetConditionListDataItemType = Literal["form_set_conditions"]

FORM_SET_CONDITION_LIST_DATA_ITEM_TYPE_VALUES: set[FormSetConditionListDataItemType] = {
    "form_set_conditions",
}


def check_form_set_condition_list_data_item_type(value: str | None) -> FormSetConditionListDataItemType | None:
    if value is None:
        return None
    if value in FORM_SET_CONDITION_LIST_DATA_ITEM_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORM_SET_CONDITION_LIST_DATA_ITEM_TYPE_VALUES!r}")
