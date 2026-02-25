from typing import Literal, cast

NewUserEmailAddressDataType = Literal["user_email_addresses"]

NEW_USER_EMAIL_ADDRESS_DATA_TYPE_VALUES: set[NewUserEmailAddressDataType] = {
    "user_email_addresses",
}


def check_new_user_email_address_data_type(value: str | None) -> NewUserEmailAddressDataType | None:
    if value is None:
        return None
    if value in NEW_USER_EMAIL_ADDRESS_DATA_TYPE_VALUES:
        return cast(NewUserEmailAddressDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_USER_EMAIL_ADDRESS_DATA_TYPE_VALUES!r}")
