from typing import Literal, cast

UpdateAuthorizationDataType = Literal["authorizations"]

UPDATE_AUTHORIZATION_DATA_TYPE_VALUES: set[UpdateAuthorizationDataType] = {
    "authorizations",
}


def check_update_authorization_data_type(value: str | None) -> UpdateAuthorizationDataType | None:
    if value is None:
        return None
    if value in UPDATE_AUTHORIZATION_DATA_TYPE_VALUES:
        return cast(UpdateAuthorizationDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_AUTHORIZATION_DATA_TYPE_VALUES!r}")
