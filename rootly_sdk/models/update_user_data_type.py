from typing import Literal

UpdateUserDataType = Literal["users"]

UPDATE_USER_DATA_TYPE_VALUES: set[UpdateUserDataType] = {
    "users",
}


def check_update_user_data_type(value: str | None) -> UpdateUserDataType | None:
    if value is None:
        return None
    if value in UPDATE_USER_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_USER_DATA_TYPE_VALUES!r}")
