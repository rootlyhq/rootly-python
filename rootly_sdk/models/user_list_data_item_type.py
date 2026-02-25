from typing import Literal, cast

UserListDataItemType = Literal["users"]

USER_LIST_DATA_ITEM_TYPE_VALUES: set[UserListDataItemType] = {
    "users",
}


def check_user_list_data_item_type(value: str | None) -> UserListDataItemType | None:
    if value is None:
        return None
    if value in USER_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(UserListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_LIST_DATA_ITEM_TYPE_VALUES!r}")
