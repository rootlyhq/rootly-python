from typing import Literal

NewStatusPageDataAttributesShowUptimeLastDays = Literal[30, 60, 90]

NEW_STATUS_PAGE_DATA_ATTRIBUTES_SHOW_UPTIME_LAST_DAYS_VALUES: set[NewStatusPageDataAttributesShowUptimeLastDays] = {
    30,
    60,
    90,
}


def check_new_status_page_data_attributes_show_uptime_last_days(
    value: int,
) -> NewStatusPageDataAttributesShowUptimeLastDays:
    if value in NEW_STATUS_PAGE_DATA_ATTRIBUTES_SHOW_UPTIME_LAST_DAYS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_STATUS_PAGE_DATA_ATTRIBUTES_SHOW_UPTIME_LAST_DAYS_VALUES!r}"
    )
