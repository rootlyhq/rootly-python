from typing import Literal, cast

NewScheduleRotationUserDataType = Literal["schedule_rotation_users"]

NEW_SCHEDULE_ROTATION_USER_DATA_TYPE_VALUES: set[NewScheduleRotationUserDataType] = {
    "schedule_rotation_users",
}


def check_new_schedule_rotation_user_data_type(value: str | None) -> NewScheduleRotationUserDataType | None:
    if value is None:
        return None
    if value in NEW_SCHEDULE_ROTATION_USER_DATA_TYPE_VALUES:
        return cast(NewScheduleRotationUserDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_SCHEDULE_ROTATION_USER_DATA_TYPE_VALUES!r}")
