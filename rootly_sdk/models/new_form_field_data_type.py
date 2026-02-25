from typing import Literal, cast

NewFormFieldDataType = Literal["form_fields"]

NEW_FORM_FIELD_DATA_TYPE_VALUES: set[NewFormFieldDataType] = {
    "form_fields",
}


def check_new_form_field_data_type(value: str | None) -> NewFormFieldDataType | None:
    if value is None:
        return None
    if value in NEW_FORM_FIELD_DATA_TYPE_VALUES:
        return cast(NewFormFieldDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_FORM_FIELD_DATA_TYPE_VALUES!r}")
