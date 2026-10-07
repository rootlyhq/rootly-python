from typing import Literal

UpdateFormFieldDataType = Literal["form_fields"]

UPDATE_FORM_FIELD_DATA_TYPE_VALUES: set[UpdateFormFieldDataType] = {
    "form_fields",
}


def check_update_form_field_data_type(value: str | None) -> UpdateFormFieldDataType | None:
    if value is None:
        return None
    if value in UPDATE_FORM_FIELD_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_FORM_FIELD_DATA_TYPE_VALUES!r}")
