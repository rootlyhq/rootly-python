from typing import Literal

NewScheduleDataType = Literal["schedules"]

NEW_SCHEDULE_DATA_TYPE_VALUES: set[NewScheduleDataType] = {
    "schedules",
}


def check_new_schedule_data_type(value: str | None) -> NewScheduleDataType | None:
    if value is None:
        return None
    if value in NEW_SCHEDULE_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_SCHEDULE_DATA_TYPE_VALUES!r}")
