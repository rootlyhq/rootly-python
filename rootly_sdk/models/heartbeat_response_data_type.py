from typing import Literal, cast

HeartbeatResponseDataType = Literal["heartbeats"]

HEARTBEAT_RESPONSE_DATA_TYPE_VALUES: set[HeartbeatResponseDataType] = {
    "heartbeats",
}


def check_heartbeat_response_data_type(value: str | None) -> HeartbeatResponseDataType | None:
    if value is None:
        return None
    if value in HEARTBEAT_RESPONSE_DATA_TYPE_VALUES:
        return cast(HeartbeatResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HEARTBEAT_RESPONSE_DATA_TYPE_VALUES!r}")
