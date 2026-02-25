from typing import Literal, cast

NewDashboardDataAttributesPeriod = Literal["day", "month", "week"]

NEW_DASHBOARD_DATA_ATTRIBUTES_PERIOD_VALUES: set[NewDashboardDataAttributesPeriod] = {
    "day",
    "month",
    "week",
}


def check_new_dashboard_data_attributes_period(value: str | None) -> NewDashboardDataAttributesPeriod | None:
    if value is None:
        return None
    if value in NEW_DASHBOARD_DATA_ATTRIBUTES_PERIOD_VALUES:
        return cast(NewDashboardDataAttributesPeriod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_DASHBOARD_DATA_ATTRIBUTES_PERIOD_VALUES!r}")
