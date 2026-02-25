from typing import Literal, cast

FormFieldListDataItemType = Literal["form_fields"]

FORM_FIELD_LIST_DATA_ITEM_TYPE_VALUES: set[FormFieldListDataItemType] = {
    "form_fields",
}


def check_form_field_list_data_item_type(value: str | None) -> FormFieldListDataItemType | None:
    if value is None:
        return None
    if value in FORM_FIELD_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(FormFieldListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORM_FIELD_LIST_DATA_ITEM_TYPE_VALUES!r}")
