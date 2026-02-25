from typing import Literal, cast

ScheduleRotationResponseDataType = Literal["schedule_rotations"]

SCHEDULE_ROTATION_RESPONSE_DATA_TYPE_VALUES: set[ScheduleRotationResponseDataType] = {
    "schedule_rotations",
}


def check_schedule_rotation_response_data_type(value: str | None) -> ScheduleRotationResponseDataType | None:
    if value is None:
        return None
    if value in SCHEDULE_ROTATION_RESPONSE_DATA_TYPE_VALUES:
        return cast(ScheduleRotationResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SCHEDULE_ROTATION_RESPONSE_DATA_TYPE_VALUES!r}")
