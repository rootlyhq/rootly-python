from typing import Literal, cast

UpdateApiKeyDataType = Literal["api_keys"]

UPDATE_API_KEY_DATA_TYPE_VALUES: set[UpdateApiKeyDataType] = {
    "api_keys",
}


def check_update_api_key_data_type(value: str | None) -> UpdateApiKeyDataType | None:
    if value is None:
        return None
    if value in UPDATE_API_KEY_DATA_TYPE_VALUES:
        return cast(UpdateApiKeyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_API_KEY_DATA_TYPE_VALUES!r}")
