from typing import Literal, cast

HeartbeatIntervalUnit = Literal["hours", "minutes"]

HEARTBEAT_INTERVAL_UNIT_VALUES: set[HeartbeatIntervalUnit] = {
    "hours",
    "minutes",
}


def check_heartbeat_interval_unit(value: str) -> HeartbeatIntervalUnit:
    if value in HEARTBEAT_INTERVAL_UNIT_VALUES:
        return cast(HeartbeatIntervalUnit, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HEARTBEAT_INTERVAL_UNIT_VALUES!r}")
