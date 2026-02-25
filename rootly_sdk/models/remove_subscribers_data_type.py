from typing import Literal, cast

RemoveSubscribersDataType = Literal["incidents"]

REMOVE_SUBSCRIBERS_DATA_TYPE_VALUES: set[RemoveSubscribersDataType] = {
    "incidents",
}


def check_remove_subscribers_data_type(value: str | None) -> RemoveSubscribersDataType | None:
    if value is None:
        return None
    if value in REMOVE_SUBSCRIBERS_DATA_TYPE_VALUES:
        return cast(RemoveSubscribersDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REMOVE_SUBSCRIBERS_DATA_TYPE_VALUES!r}")
