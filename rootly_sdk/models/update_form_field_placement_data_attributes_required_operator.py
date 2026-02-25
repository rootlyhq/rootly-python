from typing import Literal, cast

UpdateFormFieldPlacementDataAttributesRequiredOperator = Literal["and", "or"]

UPDATE_FORM_FIELD_PLACEMENT_DATA_ATTRIBUTES_REQUIRED_OPERATOR_VALUES: set[
    UpdateFormFieldPlacementDataAttributesRequiredOperator
] = {
    "and",
    "or",
}


def check_update_form_field_placement_data_attributes_required_operator(
    value: str | None,
) -> UpdateFormFieldPlacementDataAttributesRequiredOperator | None:
    if value is None:
        return None
    if value in UPDATE_FORM_FIELD_PLACEMENT_DATA_ATTRIBUTES_REQUIRED_OPERATOR_VALUES:
        return cast(UpdateFormFieldPlacementDataAttributesRequiredOperator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_FORM_FIELD_PLACEMENT_DATA_ATTRIBUTES_REQUIRED_OPERATOR_VALUES!r}"
    )
