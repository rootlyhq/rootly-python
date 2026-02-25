from typing import Literal, cast

NewScheduleRotationActiveDayDataAttributesDayName = Literal["F", "M", "R", "S", "T", "U", "W"]

NEW_SCHEDULE_ROTATION_ACTIVE_DAY_DATA_ATTRIBUTES_DAY_NAME_VALUES: set[
    NewScheduleRotationActiveDayDataAttributesDayName
] = {
    "F",
    "M",
    "R",
    "S",
    "T",
    "U",
    "W",
}


def check_new_schedule_rotation_active_day_data_attributes_day_name(
    value: str | None,
) -> NewScheduleRotationActiveDayDataAttributesDayName | None:
    if value is None:
        return None
    if value in NEW_SCHEDULE_ROTATION_ACTIVE_DAY_DATA_ATTRIBUTES_DAY_NAME_VALUES:
        return cast(NewScheduleRotationActiveDayDataAttributesDayName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_SCHEDULE_ROTATION_ACTIVE_DAY_DATA_ATTRIBUTES_DAY_NAME_VALUES!r}"
    )
