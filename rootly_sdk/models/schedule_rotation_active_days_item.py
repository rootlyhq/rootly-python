from typing import Literal, cast

ScheduleRotationActiveDaysItem = Literal["F", "M", "R", "S", "T", "U", "W"]

SCHEDULE_ROTATION_ACTIVE_DAYS_ITEM_VALUES: set[ScheduleRotationActiveDaysItem] = {
    "F",
    "M",
    "R",
    "S",
    "T",
    "U",
    "W",
}


def check_schedule_rotation_active_days_item(value: str | None) -> ScheduleRotationActiveDaysItem | None:
    if value is None:
        return None
    if value in SCHEDULE_ROTATION_ACTIVE_DAYS_ITEM_VALUES:
        return cast(ScheduleRotationActiveDaysItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SCHEDULE_ROTATION_ACTIVE_DAYS_ITEM_VALUES!r}")
