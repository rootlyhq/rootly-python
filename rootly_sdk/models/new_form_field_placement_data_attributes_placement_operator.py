from typing import Literal, cast

NewFormFieldPlacementDataAttributesPlacementOperator = Literal["and", "or"]

NEW_FORM_FIELD_PLACEMENT_DATA_ATTRIBUTES_PLACEMENT_OPERATOR_VALUES: set[
    NewFormFieldPlacementDataAttributesPlacementOperator
] = {
    "and",
    "or",
}


def check_new_form_field_placement_data_attributes_placement_operator(
    value: str | None,
) -> NewFormFieldPlacementDataAttributesPlacementOperator | None:
    if value is None:
        return None
    if value in NEW_FORM_FIELD_PLACEMENT_DATA_ATTRIBUTES_PLACEMENT_OPERATOR_VALUES:
        return cast(NewFormFieldPlacementDataAttributesPlacementOperator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_FORM_FIELD_PLACEMENT_DATA_ATTRIBUTES_PLACEMENT_OPERATOR_VALUES!r}"
    )
