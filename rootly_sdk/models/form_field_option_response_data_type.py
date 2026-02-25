from typing import Literal, cast

FormFieldOptionResponseDataType = Literal["form_field_options"]

FORM_FIELD_OPTION_RESPONSE_DATA_TYPE_VALUES: set[FormFieldOptionResponseDataType] = {
    "form_field_options",
}


def check_form_field_option_response_data_type(value: str | None) -> FormFieldOptionResponseDataType | None:
    if value is None:
        return None
    if value in FORM_FIELD_OPTION_RESPONSE_DATA_TYPE_VALUES:
        return cast(FormFieldOptionResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORM_FIELD_OPTION_RESPONSE_DATA_TYPE_VALUES!r}")
