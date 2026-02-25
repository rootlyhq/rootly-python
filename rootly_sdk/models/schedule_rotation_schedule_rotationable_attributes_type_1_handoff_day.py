from typing import Literal, cast

ScheduleRotationScheduleRotationableAttributesType1HandoffDay = Literal["F", "M", "R", "S", "T", "U", "W"]

SCHEDULE_ROTATION_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_1_HANDOFF_DAY_VALUES: set[
    ScheduleRotationScheduleRotationableAttributesType1HandoffDay
] = {
    "F",
    "M",
    "R",
    "S",
    "T",
    "U",
    "W",
}


def check_schedule_rotation_schedule_rotationable_attributes_type_1_handoff_day(
    value: str | None,
) -> ScheduleRotationScheduleRotationableAttributesType1HandoffDay | None:
    if value is None:
        return None
    if value in SCHEDULE_ROTATION_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_1_HANDOFF_DAY_VALUES:
        return cast(ScheduleRotationScheduleRotationableAttributesType1HandoffDay, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SCHEDULE_ROTATION_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_1_HANDOFF_DAY_VALUES!r}"
    )
