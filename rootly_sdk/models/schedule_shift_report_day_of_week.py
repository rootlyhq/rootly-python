from typing import Literal

ScheduleShiftReportDayOfWeek = Literal["friday", "monday", "saturday", "sunday", "thursday", "tuesday", "wednesday"]

SCHEDULE_SHIFT_REPORT_DAY_OF_WEEK_VALUES: set[ScheduleShiftReportDayOfWeek] = {
    "friday",
    "monday",
    "saturday",
    "sunday",
    "thursday",
    "tuesday",
    "wednesday",
}


def check_schedule_shift_report_day_of_week(value: str | None) -> ScheduleShiftReportDayOfWeek | None:
    if value is None:
        return None
    if value in SCHEDULE_SHIFT_REPORT_DAY_OF_WEEK_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SCHEDULE_SHIFT_REPORT_DAY_OF_WEEK_VALUES!r}")
