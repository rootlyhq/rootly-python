from typing import Literal, cast

NewFormFieldPlacementDataAttributesRequiredOperator = Literal["and", "or"]

NEW_FORM_FIELD_PLACEMENT_DATA_ATTRIBUTES_REQUIRED_OPERATOR_VALUES: set[
    NewFormFieldPlacementDataAttributesRequiredOperator
] = {
    "and",
    "or",
}


def check_new_form_field_placement_data_attributes_required_operator(
    value: str | None,
) -> NewFormFieldPlacementDataAttributesRequiredOperator | None:
    if value is None:
        return None
    if value in NEW_FORM_FIELD_PLACEMENT_DATA_ATTRIBUTES_REQUIRED_OPERATOR_VALUES:
        return cast(NewFormFieldPlacementDataAttributesRequiredOperator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_FORM_FIELD_PLACEMENT_DATA_ATTRIBUTES_REQUIRED_OPERATOR_VALUES!r}"
    )
