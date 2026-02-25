from typing import Literal, cast

FormFieldPlacementResponseDataType = Literal["form_field_placements"]

FORM_FIELD_PLACEMENT_RESPONSE_DATA_TYPE_VALUES: set[FormFieldPlacementResponseDataType] = {
    "form_field_placements",
}


def check_form_field_placement_response_data_type(value: str | None) -> FormFieldPlacementResponseDataType | None:
    if value is None:
        return None
    if value in FORM_FIELD_PLACEMENT_RESPONSE_DATA_TYPE_VALUES:
        return cast(FormFieldPlacementResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORM_FIELD_PLACEMENT_RESPONSE_DATA_TYPE_VALUES!r}")
