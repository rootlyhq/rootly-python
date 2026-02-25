from typing import Literal, cast

NewHeartbeatDataType = Literal["heartbeats"]

NEW_HEARTBEAT_DATA_TYPE_VALUES: set[NewHeartbeatDataType] = {
    "heartbeats",
}


def check_new_heartbeat_data_type(value: str | None) -> NewHeartbeatDataType | None:
    if value is None:
        return None
    if value in NEW_HEARTBEAT_DATA_TYPE_VALUES:
        return cast(NewHeartbeatDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_HEARTBEAT_DATA_TYPE_VALUES!r}")
