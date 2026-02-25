from typing import Literal, cast

UpdateCustomFieldOptionDataType = Literal["custom_field_options"]

UPDATE_CUSTOM_FIELD_OPTION_DATA_TYPE_VALUES: set[UpdateCustomFieldOptionDataType] = {
    "custom_field_options",
}


def check_update_custom_field_option_data_type(value: str | None) -> UpdateCustomFieldOptionDataType | None:
    if value is None:
        return None
    if value in UPDATE_CUSTOM_FIELD_OPTION_DATA_TYPE_VALUES:
        return cast(UpdateCustomFieldOptionDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_CUSTOM_FIELD_OPTION_DATA_TYPE_VALUES!r}")
