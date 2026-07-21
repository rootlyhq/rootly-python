from typing import Literal, cast

NewScheduleDataAttributesShiftReportDayOfWeek = Literal[
    "friday", "monday", "saturday", "sunday", "thursday", "tuesday", "wednesday"
]

NEW_SCHEDULE_DATA_ATTRIBUTES_SHIFT_REPORT_DAY_OF_WEEK_VALUES: set[NewScheduleDataAttributesShiftReportDayOfWeek] = {
    "friday",
    "monday",
    "saturday",
    "sunday",
    "thursday",
    "tuesday",
    "wednesday",
}


def check_new_schedule_data_attributes_shift_report_day_of_week(
    value: str | None,
) -> NewScheduleDataAttributesShiftReportDayOfWeek | None:
    if value is None:
        return None
    if value in NEW_SCHEDULE_DATA_ATTRIBUTES_SHIFT_REPORT_DAY_OF_WEEK_VALUES:
        return cast(NewScheduleDataAttributesShiftReportDayOfWeek, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_SCHEDULE_DATA_ATTRIBUTES_SHIFT_REPORT_DAY_OF_WEEK_VALUES!r}"
    )
