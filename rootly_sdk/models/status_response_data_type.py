from typing import Literal, cast

StatusResponseDataType = Literal["statuses"]

STATUS_RESPONSE_DATA_TYPE_VALUES: set[StatusResponseDataType] = {
    "statuses",
}


def check_status_response_data_type(value: str | None) -> StatusResponseDataType | None:
    if value is None:
        return None
    if value in STATUS_RESPONSE_DATA_TYPE_VALUES:
        return cast(StatusResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_RESPONSE_DATA_TYPE_VALUES!r}")
