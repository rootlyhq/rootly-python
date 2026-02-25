from typing import Literal, cast

UpdateScheduleRotationDataAttributesScheduleRotationableType = Literal[
    "ScheduleBiweeklyRotation",
    "ScheduleCustomRotation",
    "ScheduleDailyRotation",
    "ScheduleMonthlyRotation",
    "ScheduleWeeklyRotation",
]

UPDATE_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATIONABLE_TYPE_VALUES: set[
    UpdateScheduleRotationDataAttributesScheduleRotationableType
] = {
    "ScheduleBiweeklyRotation",
    "ScheduleCustomRotation",
    "ScheduleDailyRotation",
    "ScheduleMonthlyRotation",
    "ScheduleWeeklyRotation",
}


def check_update_schedule_rotation_data_attributes_schedule_rotationable_type(
    value: str | None,
) -> UpdateScheduleRotationDataAttributesScheduleRotationableType | None:
    if value is None:
        return None
    if value in UPDATE_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATIONABLE_TYPE_VALUES:
        return cast(UpdateScheduleRotationDataAttributesScheduleRotationableType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATIONABLE_TYPE_VALUES!r}"
    )
