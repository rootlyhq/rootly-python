from typing import Literal, cast

HeartbeatIntervalUnit = Literal["days", "hours", "minutes"]

HEARTBEAT_INTERVAL_UNIT_VALUES: set[HeartbeatIntervalUnit] = {
    "days",
    "hours",
    "minutes",
}


def check_heartbeat_interval_unit(value: str | None) -> HeartbeatIntervalUnit | None:
    if value is None:
        return None
    if value in HEARTBEAT_INTERVAL_UNIT_VALUES:
        return cast(HeartbeatIntervalUnit, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HEARTBEAT_INTERVAL_UNIT_VALUES!r}")
