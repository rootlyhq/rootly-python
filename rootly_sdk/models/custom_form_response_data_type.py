from typing import Literal, cast

CustomFormResponseDataType = Literal["custom_forms"]

CUSTOM_FORM_RESPONSE_DATA_TYPE_VALUES: set[CustomFormResponseDataType] = {
    "custom_forms",
}


def check_custom_form_response_data_type(value: str | None) -> CustomFormResponseDataType | None:
    if value is None:
        return None
    if value in CUSTOM_FORM_RESPONSE_DATA_TYPE_VALUES:
        return cast(CustomFormResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOM_FORM_RESPONSE_DATA_TYPE_VALUES!r}")
