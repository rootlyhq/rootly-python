from typing import Literal, cast

UpdateHeartbeatDataType = Literal["heartbeats"]

UPDATE_HEARTBEAT_DATA_TYPE_VALUES: set[UpdateHeartbeatDataType] = {
    "heartbeats",
}


def check_update_heartbeat_data_type(value: str | None) -> UpdateHeartbeatDataType | None:
    if value is None:
        return None
    if value in UPDATE_HEARTBEAT_DATA_TYPE_VALUES:
        return cast(UpdateHeartbeatDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_HEARTBEAT_DATA_TYPE_VALUES!r}")
