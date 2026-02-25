from typing import Literal, cast

NewUserPhoneNumberDataType = Literal["user_phone_numbers"]

NEW_USER_PHONE_NUMBER_DATA_TYPE_VALUES: set[NewUserPhoneNumberDataType] = {
    "user_phone_numbers",
}


def check_new_user_phone_number_data_type(value: str | None) -> NewUserPhoneNumberDataType | None:
    if value is None:
        return None
    if value in NEW_USER_PHONE_NUMBER_DATA_TYPE_VALUES:
        return cast(NewUserPhoneNumberDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_USER_PHONE_NUMBER_DATA_TYPE_VALUES!r}")
