from typing import Literal, cast

UpdateScheduleRotationActiveDayDataAttributesDayName = Literal["F", "M", "R", "S", "T", "U", "W"]

UPDATE_SCHEDULE_ROTATION_ACTIVE_DAY_DATA_ATTRIBUTES_DAY_NAME_VALUES: set[
    UpdateScheduleRotationActiveDayDataAttributesDayName
] = {
    "F",
    "M",
    "R",
    "S",
    "T",
    "U",
    "W",
}


def check_update_schedule_rotation_active_day_data_attributes_day_name(
    value: str | None,
) -> UpdateScheduleRotationActiveDayDataAttributesDayName | None:
    if value is None:
        return None
    if value in UPDATE_SCHEDULE_ROTATION_ACTIVE_DAY_DATA_ATTRIBUTES_DAY_NAME_VALUES:
        return cast(UpdateScheduleRotationActiveDayDataAttributesDayName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SCHEDULE_ROTATION_ACTIVE_DAY_DATA_ATTRIBUTES_DAY_NAME_VALUES!r}"
    )
