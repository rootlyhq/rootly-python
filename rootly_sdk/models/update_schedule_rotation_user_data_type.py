from typing import Literal, cast

UpdateScheduleRotationUserDataType = Literal["schedule_rotation_users"]

UPDATE_SCHEDULE_ROTATION_USER_DATA_TYPE_VALUES: set[UpdateScheduleRotationUserDataType] = {
    "schedule_rotation_users",
}


def check_update_schedule_rotation_user_data_type(value: str | None) -> UpdateScheduleRotationUserDataType | None:
    if value is None:
        return None
    if value in UPDATE_SCHEDULE_ROTATION_USER_DATA_TYPE_VALUES:
        return cast(UpdateScheduleRotationUserDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_SCHEDULE_ROTATION_USER_DATA_TYPE_VALUES!r}")
