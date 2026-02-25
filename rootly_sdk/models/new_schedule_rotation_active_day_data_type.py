from typing import Literal, cast

NewScheduleRotationActiveDayDataType = Literal["schedule_rotation_active_days"]

NEW_SCHEDULE_ROTATION_ACTIVE_DAY_DATA_TYPE_VALUES: set[NewScheduleRotationActiveDayDataType] = {
    "schedule_rotation_active_days",
}


def check_new_schedule_rotation_active_day_data_type(value: str | None) -> NewScheduleRotationActiveDayDataType | None:
    if value is None:
        return None
    if value in NEW_SCHEDULE_ROTATION_ACTIVE_DAY_DATA_TYPE_VALUES:
        return cast(NewScheduleRotationActiveDayDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_SCHEDULE_ROTATION_ACTIVE_DAY_DATA_TYPE_VALUES!r}"
    )
