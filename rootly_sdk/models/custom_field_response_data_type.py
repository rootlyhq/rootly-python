from typing import Literal, cast

CustomFieldResponseDataType = Literal["custom_fields"]

CUSTOM_FIELD_RESPONSE_DATA_TYPE_VALUES: set[CustomFieldResponseDataType] = {
    "custom_fields",
}


def check_custom_field_response_data_type(value: str | None) -> CustomFieldResponseDataType | None:
    if value is None:
        return None
    if value in CUSTOM_FIELD_RESPONSE_DATA_TYPE_VALUES:
        return cast(CustomFieldResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELD_RESPONSE_DATA_TYPE_VALUES!r}")
