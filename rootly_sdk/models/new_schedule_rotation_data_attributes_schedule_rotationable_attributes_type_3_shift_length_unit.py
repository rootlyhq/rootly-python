from typing import Literal, cast

NewScheduleRotationDataAttributesScheduleRotationableAttributesType3ShiftLengthUnit = Literal["days", "hours", "weeks"]

NEW_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_3_SHIFT_LENGTH_UNIT_VALUES: set[
    NewScheduleRotationDataAttributesScheduleRotationableAttributesType3ShiftLengthUnit
] = {
    "days",
    "hours",
    "weeks",
}


def check_new_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_3_shift_length_unit(
    value: str | None,
) -> NewScheduleRotationDataAttributesScheduleRotationableAttributesType3ShiftLengthUnit | None:
    if value is None:
        return None
    if value in NEW_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_3_SHIFT_LENGTH_UNIT_VALUES:
        return cast(NewScheduleRotationDataAttributesScheduleRotationableAttributesType3ShiftLengthUnit, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_3_SHIFT_LENGTH_UNIT_VALUES!r}"
    )
