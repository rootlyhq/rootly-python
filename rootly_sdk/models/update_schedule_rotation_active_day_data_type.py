from typing import Literal, cast

UpdateScheduleRotationActiveDayDataType = Literal["schedule_rotation_active_days"]

UPDATE_SCHEDULE_ROTATION_ACTIVE_DAY_DATA_TYPE_VALUES: set[UpdateScheduleRotationActiveDayDataType] = {
    "schedule_rotation_active_days",
}


def check_update_schedule_rotation_active_day_data_type(value: str | None) -> UpdateScheduleRotationActiveDayDataType | None:
    if value is None:
        return None
    if value in UPDATE_SCHEDULE_ROTATION_ACTIVE_DAY_DATA_TYPE_VALUES:
        return cast(UpdateScheduleRotationActiveDayDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SCHEDULE_ROTATION_ACTIVE_DAY_DATA_TYPE_VALUES!r}"
    )
