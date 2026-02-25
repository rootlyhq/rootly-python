from typing import Literal, cast

AuthorizationResponseDataType = Literal["authorizations"]

AUTHORIZATION_RESPONSE_DATA_TYPE_VALUES: set[AuthorizationResponseDataType] = {
    "authorizations",
}


def check_authorization_response_data_type(value: str | None) -> AuthorizationResponseDataType | None:
    if value is None:
        return None
    if value in AUTHORIZATION_RESPONSE_DATA_TYPE_VALUES:
        return cast(AuthorizationResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AUTHORIZATION_RESPONSE_DATA_TYPE_VALUES!r}")
