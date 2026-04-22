from typing import Literal, cast

NewApiKeyDataType = Literal["api_keys"]

NEW_API_KEY_DATA_TYPE_VALUES: set[NewApiKeyDataType] = {
    "api_keys",
}


def check_new_api_key_data_type(value: str | None) -> NewApiKeyDataType | None:
    if value is None:
        return None
    if value in NEW_API_KEY_DATA_TYPE_VALUES:
        return cast(NewApiKeyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_API_KEY_DATA_TYPE_VALUES!r}")
