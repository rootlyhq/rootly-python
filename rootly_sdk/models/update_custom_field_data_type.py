from typing import Literal, cast

UpdateCustomFieldDataType = Literal["custom_fields"]

UPDATE_CUSTOM_FIELD_DATA_TYPE_VALUES: set[UpdateCustomFieldDataType] = {
    "custom_fields",
}


def check_update_custom_field_data_type(value: str | None) -> UpdateCustomFieldDataType | None:
    if value is None:
        return None
    if value in UPDATE_CUSTOM_FIELD_DATA_TYPE_VALUES:
        return cast(UpdateCustomFieldDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_CUSTOM_FIELD_DATA_TYPE_VALUES!r}")
