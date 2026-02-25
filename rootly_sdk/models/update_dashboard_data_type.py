from typing import Literal, cast

UpdateDashboardDataType = Literal["dashboards"]

UPDATE_DASHBOARD_DATA_TYPE_VALUES: set[UpdateDashboardDataType] = {
    "dashboards",
}


def check_update_dashboard_data_type(value: str | None) -> UpdateDashboardDataType | None:
    if value is None:
        return None
    if value in UPDATE_DASHBOARD_DATA_TYPE_VALUES:
        return cast(UpdateDashboardDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_DASHBOARD_DATA_TYPE_VALUES!r}")
