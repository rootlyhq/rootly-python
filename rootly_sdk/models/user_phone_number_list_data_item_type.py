from typing import Literal, cast

UserPhoneNumberListDataItemType = Literal["user_phone_numbers"]

USER_PHONE_NUMBER_LIST_DATA_ITEM_TYPE_VALUES: set[UserPhoneNumberListDataItemType] = {
    "user_phone_numbers",
}


def check_user_phone_number_list_data_item_type(value: str | None) -> UserPhoneNumberListDataItemType | None:
    if value is None:
        return None
    if value in USER_PHONE_NUMBER_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(UserPhoneNumberListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_PHONE_NUMBER_LIST_DATA_ITEM_TYPE_VALUES!r}")
