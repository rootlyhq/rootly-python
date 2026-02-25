from typing import Literal, cast

UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType2HandoffDay = Literal[
    "first_day_of_month", "last_day_of_month"
]

UPDATE_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_2_HANDOFF_DAY_VALUES: set[
    UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType2HandoffDay
] = {
    "first_day_of_month",
    "last_day_of_month",
}


def check_update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_2_handoff_day(
    value: str | None,
) -> UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType2HandoffDay | None:
    if value is None:
        return None
    if value in UPDATE_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_2_HANDOFF_DAY_VALUES:
        return cast(UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType2HandoffDay, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_2_HANDOFF_DAY_VALUES!r}"
    )
