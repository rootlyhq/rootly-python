from typing import Literal, cast

FormSetResponseDataType = Literal["form_sets"]

FORM_SET_RESPONSE_DATA_TYPE_VALUES: set[FormSetResponseDataType] = {
    "form_sets",
}


def check_form_set_response_data_type(value: str | None) -> FormSetResponseDataType | None:
    if value is None:
        return None
    if value in FORM_SET_RESPONSE_DATA_TYPE_VALUES:
        return cast(FormSetResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORM_SET_RESPONSE_DATA_TYPE_VALUES!r}")
