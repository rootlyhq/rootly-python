from typing import Literal, cast

ScheduleRotationActiveDayResponseDataType = Literal["schedule_rotation_active_days"]

SCHEDULE_ROTATION_ACTIVE_DAY_RESPONSE_DATA_TYPE_VALUES: set[ScheduleRotationActiveDayResponseDataType] = {
    "schedule_rotation_active_days",
}


def check_schedule_rotation_active_day_response_data_type(
    value: str | None,
) -> ScheduleRotationActiveDayResponseDataType | None:
    if value is None:
        return None
    if value in SCHEDULE_ROTATION_ACTIVE_DAY_RESPONSE_DATA_TYPE_VALUES:
        return cast(ScheduleRotationActiveDayResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SCHEDULE_ROTATION_ACTIVE_DAY_RESPONSE_DATA_TYPE_VALUES!r}"
    )
