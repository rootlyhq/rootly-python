from typing import Literal, cast

UpdateFormFieldPlacementConditionDataType = Literal["form_field_placement_conditions"]

UPDATE_FORM_FIELD_PLACEMENT_CONDITION_DATA_TYPE_VALUES: set[UpdateFormFieldPlacementConditionDataType] = {
    "form_field_placement_conditions",
}


def check_update_form_field_placement_condition_data_type(
    value: str | None,
) -> UpdateFormFieldPlacementConditionDataType | None:
    if value is None:
        return None
    if value in UPDATE_FORM_FIELD_PLACEMENT_CONDITION_DATA_TYPE_VALUES:
        return cast(UpdateFormFieldPlacementConditionDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_FORM_FIELD_PLACEMENT_CONDITION_DATA_TYPE_VALUES!r}"
    )
