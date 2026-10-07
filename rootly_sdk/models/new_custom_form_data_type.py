from typing import Literal

NewCustomFormDataType = Literal["custom_forms"]

NEW_CUSTOM_FORM_DATA_TYPE_VALUES: set[NewCustomFormDataType] = {
    "custom_forms",
}


def check_new_custom_form_data_type(value: str | None) -> NewCustomFormDataType | None:
    if value is None:
        return None
    if value in NEW_CUSTOM_FORM_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_CUSTOM_FORM_DATA_TYPE_VALUES!r}")
