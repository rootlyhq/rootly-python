from typing import Literal, cast

FormFieldPlacementConditionResponseDataType = Literal["form_field_placement_conditions"]

FORM_FIELD_PLACEMENT_CONDITION_RESPONSE_DATA_TYPE_VALUES: set[FormFieldPlacementConditionResponseDataType] = {
    "form_field_placement_conditions",
}


def check_form_field_placement_condition_response_data_type(
    value: str | None,
) -> FormFieldPlacementConditionResponseDataType | None:
    if value is None:
        return None
    if value in FORM_FIELD_PLACEMENT_CONDITION_RESPONSE_DATA_TYPE_VALUES:
        return cast(FormFieldPlacementConditionResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FORM_FIELD_PLACEMENT_CONDITION_RESPONSE_DATA_TYPE_VALUES!r}"
    )
