from typing import Literal, cast

FormFieldOptionListDataItemType = Literal["form_field_options"]

FORM_FIELD_OPTION_LIST_DATA_ITEM_TYPE_VALUES: set[FormFieldOptionListDataItemType] = {
    "form_field_options",
}


def check_form_field_option_list_data_item_type(value: str | None) -> FormFieldOptionListDataItemType | None:
    if value is None:
        return None
    if value in FORM_FIELD_OPTION_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(FormFieldOptionListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORM_FIELD_OPTION_LIST_DATA_ITEM_TYPE_VALUES!r}")
