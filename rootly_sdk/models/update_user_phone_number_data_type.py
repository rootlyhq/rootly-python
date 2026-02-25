from typing import Literal, cast

UpdateUserPhoneNumberDataType = Literal["user_phone_numbers"]

UPDATE_USER_PHONE_NUMBER_DATA_TYPE_VALUES: set[UpdateUserPhoneNumberDataType] = {
    "user_phone_numbers",
}


def check_update_user_phone_number_data_type(value: str | None) -> UpdateUserPhoneNumberDataType | None:
    if value is None:
        return None
    if value in UPDATE_USER_PHONE_NUMBER_DATA_TYPE_VALUES:
        return cast(UpdateUserPhoneNumberDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_USER_PHONE_NUMBER_DATA_TYPE_VALUES!r}")
