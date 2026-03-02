from typing import Literal, cast

UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType3ShiftLengthUnit = Literal[
    "days", "hours", "weeks"
]

UPDATE_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_3_SHIFT_LENGTH_UNIT_VALUES: set[
    UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType3ShiftLengthUnit
] = {
    "days",
    "hours",
    "weeks",
}


def check_update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_3_shift_length_unit(
    value: str | None,
) -> UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType3ShiftLengthUnit | None:
    if value is None:
        return None
    if (
        value
        in UPDATE_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_3_SHIFT_LENGTH_UNIT_VALUES
    ):
        return cast(UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType3ShiftLengthUnit, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_3_SHIFT_LENGTH_UNIT_VALUES!r}"
    )
