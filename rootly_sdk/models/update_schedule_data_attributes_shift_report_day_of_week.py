from typing import Literal

UpdateScheduleDataAttributesShiftReportDayOfWeek = Literal[
    "friday", "monday", "saturday", "sunday", "thursday", "tuesday", "wednesday"
]

UPDATE_SCHEDULE_DATA_ATTRIBUTES_SHIFT_REPORT_DAY_OF_WEEK_VALUES: set[
    UpdateScheduleDataAttributesShiftReportDayOfWeek
] = {
    "friday",
    "monday",
    "saturday",
    "sunday",
    "thursday",
    "tuesday",
    "wednesday",
}


def check_update_schedule_data_attributes_shift_report_day_of_week(
    value: str | None,
) -> UpdateScheduleDataAttributesShiftReportDayOfWeek | None:
    if value is None:
        return None
    if value in UPDATE_SCHEDULE_DATA_ATTRIBUTES_SHIFT_REPORT_DAY_OF_WEEK_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SCHEDULE_DATA_ATTRIBUTES_SHIFT_REPORT_DAY_OF_WEEK_VALUES!r}"
    )
