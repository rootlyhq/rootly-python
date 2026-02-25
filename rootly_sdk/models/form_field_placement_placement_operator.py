from typing import Literal, cast

FormFieldPlacementPlacementOperator = Literal["and", "or"]

FORM_FIELD_PLACEMENT_PLACEMENT_OPERATOR_VALUES: set[FormFieldPlacementPlacementOperator] = {
    "and",
    "or",
}


def check_form_field_placement_placement_operator(value: str | None) -> FormFieldPlacementPlacementOperator | None:
    if value is None:
        return None
    if value in FORM_FIELD_PLACEMENT_PLACEMENT_OPERATOR_VALUES:
        return cast(FormFieldPlacementPlacementOperator, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORM_FIELD_PLACEMENT_PLACEMENT_OPERATOR_VALUES!r}")
