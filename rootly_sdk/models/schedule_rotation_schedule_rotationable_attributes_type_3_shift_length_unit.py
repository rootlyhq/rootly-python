from typing import Literal, cast

ScheduleRotationScheduleRotationableAttributesType3ShiftLengthUnit = Literal["days", "hours", "weeks"]

SCHEDULE_ROTATION_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_3_SHIFT_LENGTH_UNIT_VALUES: set[
    ScheduleRotationScheduleRotationableAttributesType3ShiftLengthUnit
] = {
    "days",
    "hours",
    "weeks",
}


def check_schedule_rotation_schedule_rotationable_attributes_type_3_shift_length_unit(
    value: str | None,
) -> ScheduleRotationScheduleRotationableAttributesType3ShiftLengthUnit | None:
    if value is None:
        return None
    if value in SCHEDULE_ROTATION_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_3_SHIFT_LENGTH_UNIT_VALUES:
        return cast(ScheduleRotationScheduleRotationableAttributesType3ShiftLengthUnit, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SCHEDULE_ROTATION_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_3_SHIFT_LENGTH_UNIT_VALUES!r}"
    )
