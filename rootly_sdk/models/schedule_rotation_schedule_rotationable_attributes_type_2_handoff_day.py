from typing import Literal, cast

ScheduleRotationScheduleRotationableAttributesType2HandoffDay = Literal["first_day_of_month", "last_day_of_month"]

SCHEDULE_ROTATION_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_2_HANDOFF_DAY_VALUES: set[
    ScheduleRotationScheduleRotationableAttributesType2HandoffDay
] = {
    "first_day_of_month",
    "last_day_of_month",
}


def check_schedule_rotation_schedule_rotationable_attributes_type_2_handoff_day(
    value: str | None,
) -> ScheduleRotationScheduleRotationableAttributesType2HandoffDay | None:
    if value is None:
        return None
    if value in SCHEDULE_ROTATION_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_2_HANDOFF_DAY_VALUES:
        return cast(ScheduleRotationScheduleRotationableAttributesType2HandoffDay, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SCHEDULE_ROTATION_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_2_HANDOFF_DAY_VALUES!r}"
    )
