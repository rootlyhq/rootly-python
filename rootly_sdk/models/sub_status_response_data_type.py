from typing import Literal, cast

SubStatusResponseDataType = Literal["sub_statuses"]

SUB_STATUS_RESPONSE_DATA_TYPE_VALUES: set[SubStatusResponseDataType] = {
    "sub_statuses",
}


def check_sub_status_response_data_type(value: str | None) -> SubStatusResponseDataType | None:
    if value is None:
        return None
    if value in SUB_STATUS_RESPONSE_DATA_TYPE_VALUES:
        return cast(SubStatusResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SUB_STATUS_RESPONSE_DATA_TYPE_VALUES!r}")
