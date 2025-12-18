from typing import Literal, cast

UpdateHeartbeatDataAttributesIntervalUnit = Literal["hours", "minutes"]

UPDATE_HEARTBEAT_DATA_ATTRIBUTES_INTERVAL_UNIT_VALUES: set[UpdateHeartbeatDataAttributesIntervalUnit] = {
    "hours",
    "minutes",
}


def check_update_heartbeat_data_attributes_interval_unit(value: str) -> UpdateHeartbeatDataAttributesIntervalUnit:
    if value in UPDATE_HEARTBEAT_DATA_ATTRIBUTES_INTERVAL_UNIT_VALUES:
        return cast(UpdateHeartbeatDataAttributesIntervalUnit, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_HEARTBEAT_DATA_ATTRIBUTES_INTERVAL_UNIT_VALUES!r}"
    )
