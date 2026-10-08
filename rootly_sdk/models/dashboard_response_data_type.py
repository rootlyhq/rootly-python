from typing import Literal

DashboardResponseDataType = Literal["dashboards"]

DASHBOARD_RESPONSE_DATA_TYPE_VALUES: set[DashboardResponseDataType] = {
    "dashboards",
}


def check_dashboard_response_data_type(value: str | None) -> DashboardResponseDataType | None:
    if value is None:
        return None
    if value in DASHBOARD_RESPONSE_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DASHBOARD_RESPONSE_DATA_TYPE_VALUES!r}")
