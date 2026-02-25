from typing import Literal, cast

FormFieldPlacementRequiredOperator = Literal["and", "or"]

FORM_FIELD_PLACEMENT_REQUIRED_OPERATOR_VALUES: set[FormFieldPlacementRequiredOperator] = {
    "and",
    "or",
}


def check_form_field_placement_required_operator(value: str | None) -> FormFieldPlacementRequiredOperator | None:
    if value is None:
        return None
    if value in FORM_FIELD_PLACEMENT_REQUIRED_OPERATOR_VALUES:
        return cast(FormFieldPlacementRequiredOperator, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORM_FIELD_PLACEMENT_REQUIRED_OPERATOR_VALUES!r}")
