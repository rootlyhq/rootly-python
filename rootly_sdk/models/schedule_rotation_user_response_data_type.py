from typing import Literal, cast

ScheduleRotationUserResponseDataType = Literal["schedule_rotation_users"]

SCHEDULE_ROTATION_USER_RESPONSE_DATA_TYPE_VALUES: set[ScheduleRotationUserResponseDataType] = {
    "schedule_rotation_users",
}


def check_schedule_rotation_user_response_data_type(value: str | None) -> ScheduleRotationUserResponseDataType | None:
    if value is None:
        return None
    if value in SCHEDULE_ROTATION_USER_RESPONSE_DATA_TYPE_VALUES:
        return cast(ScheduleRotationUserResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SCHEDULE_ROTATION_USER_RESPONSE_DATA_TYPE_VALUES!r}")
