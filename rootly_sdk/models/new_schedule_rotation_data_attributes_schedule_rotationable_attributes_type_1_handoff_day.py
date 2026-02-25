from typing import Literal, cast

NewScheduleRotationDataAttributesScheduleRotationableAttributesType1HandoffDay = Literal[
    "F", "M", "R", "S", "T", "U", "W"
]

NEW_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_1_HANDOFF_DAY_VALUES: set[
    NewScheduleRotationDataAttributesScheduleRotationableAttributesType1HandoffDay
] = {
    "F",
    "M",
    "R",
    "S",
    "T",
    "U",
    "W",
}


def check_new_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_1_handoff_day(
    value: str | None,
) -> NewScheduleRotationDataAttributesScheduleRotationableAttributesType1HandoffDay | None:
    if value is None:
        return None
    if value in NEW_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_1_HANDOFF_DAY_VALUES:
        return cast(NewScheduleRotationDataAttributesScheduleRotationableAttributesType1HandoffDay, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATIONABLE_ATTRIBUTES_TYPE_1_HANDOFF_DAY_VALUES!r}"
    )
