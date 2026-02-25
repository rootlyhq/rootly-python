from typing import Literal, cast

FormFieldPositionResponseDataType = Literal["form_field_positions"]

FORM_FIELD_POSITION_RESPONSE_DATA_TYPE_VALUES: set[FormFieldPositionResponseDataType] = {
    "form_field_positions",
}


def check_form_field_position_response_data_type(value: str | None) -> FormFieldPositionResponseDataType | None:
    if value is None:
        return None
    if value in FORM_FIELD_POSITION_RESPONSE_DATA_TYPE_VALUES:
        return cast(FormFieldPositionResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORM_FIELD_POSITION_RESPONSE_DATA_TYPE_VALUES!r}")
