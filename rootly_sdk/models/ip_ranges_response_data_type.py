from typing import Literal, cast

IpRangesResponseDataType = Literal["ip_ranges"]

IP_RANGES_RESPONSE_DATA_TYPE_VALUES: set[IpRangesResponseDataType] = {
    "ip_ranges",
}


def check_ip_ranges_response_data_type(value: str | None) -> IpRangesResponseDataType | None:
    if value is None:
        return None
    if value in IP_RANGES_RESPONSE_DATA_TYPE_VALUES:
        return cast(IpRangesResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IP_RANGES_RESPONSE_DATA_TYPE_VALUES!r}")
