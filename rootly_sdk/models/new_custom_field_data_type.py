from typing import Literal, cast

NewCustomFieldDataType = Literal["custom_fields"]

NEW_CUSTOM_FIELD_DATA_TYPE_VALUES: set[NewCustomFieldDataType] = {
    "custom_fields",
}


def check_new_custom_field_data_type(value: str | None) -> NewCustomFieldDataType | None:
    if value is None:
        return None
    if value in NEW_CUSTOM_FIELD_DATA_TYPE_VALUES:
        return cast(NewCustomFieldDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_CUSTOM_FIELD_DATA_TYPE_VALUES!r}")
