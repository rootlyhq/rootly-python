from typing import Literal, cast

SecretResponseDataType = Literal["secrets"]

SECRET_RESPONSE_DATA_TYPE_VALUES: set[SecretResponseDataType] = {
    "secrets",
}


def check_secret_response_data_type(value: str | None) -> SecretResponseDataType | None:
    if value is None:
        return None
    if value in SECRET_RESPONSE_DATA_TYPE_VALUES:
        return cast(SecretResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SECRET_RESPONSE_DATA_TYPE_VALUES!r}")
