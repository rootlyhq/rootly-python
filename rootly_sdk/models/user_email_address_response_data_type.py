from typing import Literal, cast

UserEmailAddressResponseDataType = Literal["user_email_addresses"]

USER_EMAIL_ADDRESS_RESPONSE_DATA_TYPE_VALUES: set[UserEmailAddressResponseDataType] = {
    "user_email_addresses",
}


def check_user_email_address_response_data_type(value: str | None) -> UserEmailAddressResponseDataType | None:
    if value is None:
        return None
    if value in USER_EMAIL_ADDRESS_RESPONSE_DATA_TYPE_VALUES:
        return cast(UserEmailAddressResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_EMAIL_ADDRESS_RESPONSE_DATA_TYPE_VALUES!r}")
