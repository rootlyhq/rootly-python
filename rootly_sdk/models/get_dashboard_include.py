from typing import Literal, cast

GetDashboardInclude = Literal["panels"]

GET_DASHBOARD_INCLUDE_VALUES: set[GetDashboardInclude] = {
    "panels",
}


def check_get_dashboard_include(value: str | None) -> GetDashboardInclude | None:
    if value is None:
        return None
    if value in GET_DASHBOARD_INCLUDE_VALUES:
        return cast(GetDashboardInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_DASHBOARD_INCLUDE_VALUES!r}")
