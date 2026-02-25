from typing import Literal, cast

FormFieldPlacementConditionListDataItemType = Literal["form_field_placement_conditions"]

FORM_FIELD_PLACEMENT_CONDITION_LIST_DATA_ITEM_TYPE_VALUES: set[FormFieldPlacementConditionListDataItemType] = {
    "form_field_placement_conditions",
}


def check_form_field_placement_condition_list_data_item_type(
    value: str | None,
) -> FormFieldPlacementConditionListDataItemType | None:
    if value is None:
        return None
    if value in FORM_FIELD_PLACEMENT_CONDITION_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(FormFieldPlacementConditionListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FORM_FIELD_PLACEMENT_CONDITION_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
