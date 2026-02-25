from typing import Literal, cast

NewHeartbeatDataAttributesIntervalUnit = Literal["days", "hours", "minutes"]

NEW_HEARTBEAT_DATA_ATTRIBUTES_INTERVAL_UNIT_VALUES: set[NewHeartbeatDataAttributesIntervalUnit] = {
    "days",
    "hours",
    "minutes",
}


def check_new_heartbeat_data_attributes_interval_unit(
    value: str | None,
) -> NewHeartbeatDataAttributesIntervalUnit | None:
    if value is None:
        return None
    if value in NEW_HEARTBEAT_DATA_ATTRIBUTES_INTERVAL_UNIT_VALUES:
        return cast(NewHeartbeatDataAttributesIntervalUnit, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_HEARTBEAT_DATA_ATTRIBUTES_INTERVAL_UNIT_VALUES!r}"
    )
