from typing import Literal, cast

AddSubscribersDataType = Literal["incidents"]

ADD_SUBSCRIBERS_DATA_TYPE_VALUES: set[AddSubscribersDataType] = {
    "incidents",
}


def check_add_subscribers_data_type(value: str | None) -> AddSubscribersDataType | None:
    if value is None:
        return None
    if value in ADD_SUBSCRIBERS_DATA_TYPE_VALUES:
        return cast(AddSubscribersDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ADD_SUBSCRIBERS_DATA_TYPE_VALUES!r}")
