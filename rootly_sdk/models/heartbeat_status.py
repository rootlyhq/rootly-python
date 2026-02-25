from typing import Literal, cast

HeartbeatStatus = Literal["active", "expired", "waiting"]

HEARTBEAT_STATUS_VALUES: set[HeartbeatStatus] = {
    "active",
    "expired",
    "waiting",
}


def check_heartbeat_status(value: str | None) -> HeartbeatStatus | None:
    if value is None:
        return None
    if value in HEARTBEAT_STATUS_VALUES:
        return cast(HeartbeatStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HEARTBEAT_STATUS_VALUES!r}")
