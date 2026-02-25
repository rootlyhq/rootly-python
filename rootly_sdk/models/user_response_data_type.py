from typing import Literal, cast

UserResponseDataType = Literal["users"]

USER_RESPONSE_DATA_TYPE_VALUES: set[UserResponseDataType] = {
    "users",
}


def check_user_response_data_type(value: str | None) -> UserResponseDataType | None:
    if value is None:
        return None
    if value in USER_RESPONSE_DATA_TYPE_VALUES:
        return cast(UserResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_RESPONSE_DATA_TYPE_VALUES!r}")
