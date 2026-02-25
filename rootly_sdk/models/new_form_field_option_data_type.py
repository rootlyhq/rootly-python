from typing import Literal, cast

NewFormFieldOptionDataType = Literal["form_field_options"]

NEW_FORM_FIELD_OPTION_DATA_TYPE_VALUES: set[NewFormFieldOptionDataType] = {
    "form_field_options",
}


def check_new_form_field_option_data_type(value: str | None) -> NewFormFieldOptionDataType | None:
    if value is None:
        return None
    if value in NEW_FORM_FIELD_OPTION_DATA_TYPE_VALUES:
        return cast(NewFormFieldOptionDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_FORM_FIELD_OPTION_DATA_TYPE_VALUES!r}")
