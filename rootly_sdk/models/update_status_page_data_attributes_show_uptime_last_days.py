from typing import Literal

UpdateStatusPageDataAttributesShowUptimeLastDays = Literal[30, 60, 90]

UPDATE_STATUS_PAGE_DATA_ATTRIBUTES_SHOW_UPTIME_LAST_DAYS_VALUES: set[
    UpdateStatusPageDataAttributesShowUptimeLastDays
] = {
    30,
    60,
    90,
}


def check_update_status_page_data_attributes_show_uptime_last_days(
    value: int,
) -> UpdateStatusPageDataAttributesShowUptimeLastDays:
    if value in UPDATE_STATUS_PAGE_DATA_ATTRIBUTES_SHOW_UPTIME_LAST_DAYS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_STATUS_PAGE_DATA_ATTRIBUTES_SHOW_UPTIME_LAST_DAYS_VALUES!r}"
    )
