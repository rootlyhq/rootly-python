from typing import Literal, cast

RotateApiKeyDataType = Literal["api_keys"]

ROTATE_API_KEY_DATA_TYPE_VALUES: set[RotateApiKeyDataType] = {
    "api_keys",
}


def check_rotate_api_key_data_type(value: str | None) -> RotateApiKeyDataType | None:
    if value is None:
        return None
    if value in ROTATE_API_KEY_DATA_TYPE_VALUES:
        return cast(RotateApiKeyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROTATE_API_KEY_DATA_TYPE_VALUES!r}")
