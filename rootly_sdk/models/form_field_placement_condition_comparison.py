from typing import Literal, cast

FormFieldPlacementConditionComparison = Literal["equal", "is_not_set", "is_set", "not_equal"]

FORM_FIELD_PLACEMENT_CONDITION_COMPARISON_VALUES: set[FormFieldPlacementConditionComparison] = {
    "equal",
    "is_not_set",
    "is_set",
    "not_equal",
}


def check_form_field_placement_condition_comparison(value: str | None) -> FormFieldPlacementConditionComparison | None:
    if value is None:
        return None
    if value in FORM_FIELD_PLACEMENT_CONDITION_COMPARISON_VALUES:
        return cast(FormFieldPlacementConditionComparison, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORM_FIELD_PLACEMENT_CONDITION_COMPARISON_VALUES!r}")
