from typing import Literal, cast

UpdateDashboardDataAttributesPeriod = Literal["day", "month", "week"]

UPDATE_DASHBOARD_DATA_ATTRIBUTES_PERIOD_VALUES: set[UpdateDashboardDataAttributesPeriod] = {
    "day",
    "month",
    "week",
}


def check_update_dashboard_data_attributes_period(value: str | None) -> UpdateDashboardDataAttributesPeriod | None:
    if value is None:
        return None
    if value in UPDATE_DASHBOARD_DATA_ATTRIBUTES_PERIOD_VALUES:
        return cast(UpdateDashboardDataAttributesPeriod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_DASHBOARD_DATA_ATTRIBUTES_PERIOD_VALUES!r}")
