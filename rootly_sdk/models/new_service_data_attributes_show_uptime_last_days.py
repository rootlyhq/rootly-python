from typing import Literal

NewServiceDataAttributesShowUptimeLastDays = Literal[30, 60, 90]

NEW_SERVICE_DATA_ATTRIBUTES_SHOW_UPTIME_LAST_DAYS_VALUES: set[NewServiceDataAttributesShowUptimeLastDays] = {
    30,
    60,
    90,
}


def check_new_service_data_attributes_show_uptime_last_days(value: int) -> NewServiceDataAttributesShowUptimeLastDays:
    if value in NEW_SERVICE_DATA_ATTRIBUTES_SHOW_UPTIME_LAST_DAYS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_SERVICE_DATA_ATTRIBUTES_SHOW_UPTIME_LAST_DAYS_VALUES!r}"
    )
