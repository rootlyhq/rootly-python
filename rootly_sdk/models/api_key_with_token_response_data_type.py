from typing import Literal, cast

ApiKeyWithTokenResponseDataType = Literal["api_keys"]

API_KEY_WITH_TOKEN_RESPONSE_DATA_TYPE_VALUES: set[ApiKeyWithTokenResponseDataType] = {
    "api_keys",
}


def check_api_key_with_token_response_data_type(value: str | None) -> ApiKeyWithTokenResponseDataType | None:
    if value is None:
        return None
    if value in API_KEY_WITH_TOKEN_RESPONSE_DATA_TYPE_VALUES:
        return cast(ApiKeyWithTokenResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_KEY_WITH_TOKEN_RESPONSE_DATA_TYPE_VALUES!r}")
