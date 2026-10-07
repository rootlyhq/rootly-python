from typing import Literal

StatusPageShowUptimeLastDays = Literal[30, 60, 90]

STATUS_PAGE_SHOW_UPTIME_LAST_DAYS_VALUES: set[StatusPageShowUptimeLastDays] = {
    30,
    60,
    90,
}


def check_status_page_show_uptime_last_days(value: int) -> StatusPageShowUptimeLastDays:
    if value in STATUS_PAGE_SHOW_UPTIME_LAST_DAYS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_SHOW_UPTIME_LAST_DAYS_VALUES!r}")
