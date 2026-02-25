from typing import Literal, cast

NewDashboardDataType = Literal["dashboards"]

NEW_DASHBOARD_DATA_TYPE_VALUES: set[NewDashboardDataType] = {
    "dashboards",
}


def check_new_dashboard_data_type(value: str | None) -> NewDashboardDataType | None:
    if value is None:
        return None
    if value in NEW_DASHBOARD_DATA_TYPE_VALUES:
        return cast(NewDashboardDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_DASHBOARD_DATA_TYPE_VALUES!r}")
