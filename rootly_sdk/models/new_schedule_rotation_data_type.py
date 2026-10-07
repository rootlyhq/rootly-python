from typing import Literal

NewScheduleRotationDataType = Literal["schedule_rotations"]

NEW_SCHEDULE_ROTATION_DATA_TYPE_VALUES: set[NewScheduleRotationDataType] = {
    "schedule_rotations",
}


def check_new_schedule_rotation_data_type(value: str | None) -> NewScheduleRotationDataType | None:
    if value is None:
        return None
    if value in NEW_SCHEDULE_ROTATION_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_SCHEDULE_ROTATION_DATA_TYPE_VALUES!r}")
