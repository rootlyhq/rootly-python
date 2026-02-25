from typing import Literal, cast

NewFormFieldPlacementConditionDataType = Literal["form_field_placement_conditions"]

NEW_FORM_FIELD_PLACEMENT_CONDITION_DATA_TYPE_VALUES: set[NewFormFieldPlacementConditionDataType] = {
    "form_field_placement_conditions",
}


def check_new_form_field_placement_condition_data_type(value: str | None) -> NewFormFieldPlacementConditionDataType | None:
    if value is None:
        return None
    if value in NEW_FORM_FIELD_PLACEMENT_CONDITION_DATA_TYPE_VALUES:
        return cast(NewFormFieldPlacementConditionDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_FORM_FIELD_PLACEMENT_CONDITION_DATA_TYPE_VALUES!r}"
    )
