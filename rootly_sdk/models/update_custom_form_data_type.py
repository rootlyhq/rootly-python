from typing import Literal, cast

UpdateCustomFormDataType = Literal["custom_forms"]

UPDATE_CUSTOM_FORM_DATA_TYPE_VALUES: set[UpdateCustomFormDataType] = {
    "custom_forms",
}


def check_update_custom_form_data_type(value: str | None) -> UpdateCustomFormDataType | None:
    if value is None:
        return None
    if value in UPDATE_CUSTOM_FORM_DATA_TYPE_VALUES:
        return cast(UpdateCustomFormDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_CUSTOM_FORM_DATA_TYPE_VALUES!r}")
