from typing import Literal, cast

NewAuthorizationDataType = Literal["authorizations"]

NEW_AUTHORIZATION_DATA_TYPE_VALUES: set[NewAuthorizationDataType] = {
    "authorizations",
}


def check_new_authorization_data_type(value: str | None) -> NewAuthorizationDataType | None:
    if value is None:
        return None
    if value in NEW_AUTHORIZATION_DATA_TYPE_VALUES:
        return cast(NewAuthorizationDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_AUTHORIZATION_DATA_TYPE_VALUES!r}")
