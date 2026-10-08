from typing import Literal

NewFunctionalityDataAttributesShowUptimeLastDays = Literal[30, 60, 90]

NEW_FUNCTIONALITY_DATA_ATTRIBUTES_SHOW_UPTIME_LAST_DAYS_VALUES: set[
    NewFunctionalityDataAttributesShowUptimeLastDays
] = {
    30,
    60,
    90,
}


def check_new_functionality_data_attributes_show_uptime_last_days(
    value: int,
) -> NewFunctionalityDataAttributesShowUptimeLastDays:
    if value in NEW_FUNCTIONALITY_DATA_ATTRIBUTES_SHOW_UPTIME_LAST_DAYS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_FUNCTIONALITY_DATA_ATTRIBUTES_SHOW_UPTIME_LAST_DAYS_VALUES!r}"
    )
