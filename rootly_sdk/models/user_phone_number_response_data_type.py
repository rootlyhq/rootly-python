from typing import Literal, cast

UserPhoneNumberResponseDataType = Literal["user_phone_numbers"]

USER_PHONE_NUMBER_RESPONSE_DATA_TYPE_VALUES: set[UserPhoneNumberResponseDataType] = {
    "user_phone_numbers",
}


def check_user_phone_number_response_data_type(value: str | None) -> UserPhoneNumberResponseDataType | None:
    if value is None:
        return None
    if value in USER_PHONE_NUMBER_RESPONSE_DATA_TYPE_VALUES:
        return cast(UserPhoneNumberResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_PHONE_NUMBER_RESPONSE_DATA_TYPE_VALUES!r}")
