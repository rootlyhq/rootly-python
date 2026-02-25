from typing import Literal, cast

UpdateFormFieldOptionDataType = Literal["form_field_options"]

UPDATE_FORM_FIELD_OPTION_DATA_TYPE_VALUES: set[UpdateFormFieldOptionDataType] = {
    "form_field_options",
}


def check_update_form_field_option_data_type(value: str | None) -> UpdateFormFieldOptionDataType | None:
    if value is None:
        return None
    if value in UPDATE_FORM_FIELD_OPTION_DATA_TYPE_VALUES:
        return cast(UpdateFormFieldOptionDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_FORM_FIELD_OPTION_DATA_TYPE_VALUES!r}")
