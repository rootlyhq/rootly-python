from typing import Literal, cast

NewFormFieldPlacementConditionDataAttributesComparison = Literal["equal", "is_not_set", "is_set", "not_equal"]

NEW_FORM_FIELD_PLACEMENT_CONDITION_DATA_ATTRIBUTES_COMPARISON_VALUES: set[
    NewFormFieldPlacementConditionDataAttributesComparison
] = {
    "equal",
    "is_not_set",
    "is_set",
    "not_equal",
}


def check_new_form_field_placement_condition_data_attributes_comparison(
    value: str | None,
) -> NewFormFieldPlacementConditionDataAttributesComparison | None:
    if value is None:
        return None
    if value in NEW_FORM_FIELD_PLACEMENT_CONDITION_DATA_ATTRIBUTES_COMPARISON_VALUES:
        return cast(NewFormFieldPlacementConditionDataAttributesComparison, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_FORM_FIELD_PLACEMENT_CONDITION_DATA_ATTRIBUTES_COMPARISON_VALUES!r}"
    )
