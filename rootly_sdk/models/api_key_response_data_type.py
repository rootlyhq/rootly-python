from typing import Literal, cast

ApiKeyResponseDataType = Literal["api_keys"]

API_KEY_RESPONSE_DATA_TYPE_VALUES: set[ApiKeyResponseDataType] = {
    "api_keys",
}


def check_api_key_response_data_type(value: str | None) -> ApiKeyResponseDataType | None:
    if value is None:
        return None
    if value in API_KEY_RESPONSE_DATA_TYPE_VALUES:
        return cast(ApiKeyResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_KEY_RESPONSE_DATA_TYPE_VALUES!r}")
