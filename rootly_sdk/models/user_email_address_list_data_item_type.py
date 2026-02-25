from typing import Literal, cast

UserEmailAddressListDataItemType = Literal["user_email_addresses"]

USER_EMAIL_ADDRESS_LIST_DATA_ITEM_TYPE_VALUES: set[UserEmailAddressListDataItemType] = {
    "user_email_addresses",
}


def check_user_email_address_list_data_item_type(value: str | None) -> UserEmailAddressListDataItemType | None:
    if value is None:
        return None
    if value in USER_EMAIL_ADDRESS_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(UserEmailAddressListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_EMAIL_ADDRESS_LIST_DATA_ITEM_TYPE_VALUES!r}")
