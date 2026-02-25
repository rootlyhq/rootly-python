from typing import Literal, cast

UpdateFormFieldPlacementConditionDataAttributesComparison = Literal["equal", "is_not_set", "is_set", "not_equal"]

UPDATE_FORM_FIELD_PLACEMENT_CONDITION_DATA_ATTRIBUTES_COMPARISON_VALUES: set[
    UpdateFormFieldPlacementConditionDataAttributesComparison
] = {
    "equal",
    "is_not_set",
    "is_set",
    "not_equal",
}


def check_update_form_field_placement_condition_data_attributes_comparison(
    value: str | None,
) -> UpdateFormFieldPlacementConditionDataAttributesComparison | None:
    if value is None:
        return None
    if value in UPDATE_FORM_FIELD_PLACEMENT_CONDITION_DATA_ATTRIBUTES_COMPARISON_VALUES:
        return cast(UpdateFormFieldPlacementConditionDataAttributesComparison, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_FORM_FIELD_PLACEMENT_CONDITION_DATA_ATTRIBUTES_COMPARISON_VALUES!r}"
    )
