from typing import Literal, cast

CustomFieldOptionResponseDataType = Literal["custom_field_options"]

CUSTOM_FIELD_OPTION_RESPONSE_DATA_TYPE_VALUES: set[CustomFieldOptionResponseDataType] = {
    "custom_field_options",
}


def check_custom_field_option_response_data_type(value: str | None) -> CustomFieldOptionResponseDataType | None:
    if value is None:
        return None
    if value in CUSTOM_FIELD_OPTION_RESPONSE_DATA_TYPE_VALUES:
        return cast(CustomFieldOptionResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELD_OPTION_RESPONSE_DATA_TYPE_VALUES!r}")
