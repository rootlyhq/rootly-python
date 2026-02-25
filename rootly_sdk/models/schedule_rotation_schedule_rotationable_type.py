from typing import Literal, cast

ScheduleRotationScheduleRotationableType = Literal[
    "ScheduleBiweeklyRotation",
    "ScheduleCustomRotation",
    "ScheduleDailyRotation",
    "ScheduleMonthlyRotation",
    "ScheduleWeeklyRotation",
]

SCHEDULE_ROTATION_SCHEDULE_ROTATIONABLE_TYPE_VALUES: set[ScheduleRotationScheduleRotationableType] = {
    "ScheduleBiweeklyRotation",
    "ScheduleCustomRotation",
    "ScheduleDailyRotation",
    "ScheduleMonthlyRotation",
    "ScheduleWeeklyRotation",
}


def check_schedule_rotation_schedule_rotationable_type(value: str | None) -> ScheduleRotationScheduleRotationableType | None:
    if value is None:
        return None
    if value in SCHEDULE_ROTATION_SCHEDULE_ROTATIONABLE_TYPE_VALUES:
        return cast(ScheduleRotationScheduleRotationableType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SCHEDULE_ROTATION_SCHEDULE_ROTATIONABLE_TYPE_VALUES!r}"
    )
