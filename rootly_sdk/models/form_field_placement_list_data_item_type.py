from typing import Literal, cast

FormFieldPlacementListDataItemType = Literal["form_field_placements"]

FORM_FIELD_PLACEMENT_LIST_DATA_ITEM_TYPE_VALUES: set[FormFieldPlacementListDataItemType] = {
    "form_field_placements",
}


def check_form_field_placement_list_data_item_type(value: str | None) -> FormFieldPlacementListDataItemType | None:
    if value is None:
        return None
    if value in FORM_FIELD_PLACEMENT_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(FormFieldPlacementListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORM_FIELD_PLACEMENT_LIST_DATA_ITEM_TYPE_VALUES!r}")
