from typing import Literal, cast

UpdateScheduleDataType = Literal["schedules"]

UPDATE_SCHEDULE_DATA_TYPE_VALUES: set[UpdateScheduleDataType] = {
    "schedules",
}


def check_update_schedule_data_type(value: str | None) -> UpdateScheduleDataType | None:
    if value is None:
        return None
    if value in UPDATE_SCHEDULE_DATA_TYPE_VALUES:
        return cast(UpdateScheduleDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_SCHEDULE_DATA_TYPE_VALUES!r}")
