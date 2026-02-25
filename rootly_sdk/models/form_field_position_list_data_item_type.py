from typing import Literal, cast

FormFieldPositionListDataItemType = Literal["form_field_positions"]

FORM_FIELD_POSITION_LIST_DATA_ITEM_TYPE_VALUES: set[FormFieldPositionListDataItemType] = {
    "form_field_positions",
}


def check_form_field_position_list_data_item_type(value: str | None) -> FormFieldPositionListDataItemType | None:
    if value is None:
        return None
    if value in FORM_FIELD_POSITION_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(FormFieldPositionListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORM_FIELD_POSITION_LIST_DATA_ITEM_TYPE_VALUES!r}")
