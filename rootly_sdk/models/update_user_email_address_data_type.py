from typing import Literal, cast

UpdateUserEmailAddressDataType = Literal["user_email_addresses"]

UPDATE_USER_EMAIL_ADDRESS_DATA_TYPE_VALUES: set[UpdateUserEmailAddressDataType] = {
    "user_email_addresses",
}


def check_update_user_email_address_data_type(value: str | None) -> UpdateUserEmailAddressDataType | None:
    if value is None:
        return None
    if value in UPDATE_USER_EMAIL_ADDRESS_DATA_TYPE_VALUES:
        return cast(UpdateUserEmailAddressDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_USER_EMAIL_ADDRESS_DATA_TYPE_VALUES!r}")
