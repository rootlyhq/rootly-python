from typing import Literal, cast

FormFieldResponseDataType = Literal["form_fields"]

FORM_FIELD_RESPONSE_DATA_TYPE_VALUES: set[FormFieldResponseDataType] = {
    "form_fields",
}


def check_form_field_response_data_type(value: str | None) -> FormFieldResponseDataType | None:
    if value is None:
        return None
    if value in FORM_FIELD_RESPONSE_DATA_TYPE_VALUES:
        return cast(FormFieldResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORM_FIELD_RESPONSE_DATA_TYPE_VALUES!r}")
