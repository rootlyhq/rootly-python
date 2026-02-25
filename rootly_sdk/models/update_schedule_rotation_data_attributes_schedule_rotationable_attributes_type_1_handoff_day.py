from typing import Literal, cast

UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1HandoffDay = Literal[
    "F", "M", "R", "S", "T", "U", "W"
]

UPDATE_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_1_HANDOFF_DAY_VALUES: set[
    UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1HandoffDay
] = {
    "F",
    "M",
    "R",
    "S",
    "T",
    "U",
    "W",
}


def check_update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_1_handoff_day(
    value: str | None,
) -> UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1HandoffDay | None:
    if value is None:
        return None
    if value in UPDATE_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_1_HANDOFF_DAY_VALUES:
        return cast(UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1HandoffDay, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_1_HANDOFF_DAY_VALUES!r}"
    )
