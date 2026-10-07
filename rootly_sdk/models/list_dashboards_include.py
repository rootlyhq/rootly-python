from typing import Literal

ListDashboardsInclude = Literal["panels"]

LIST_DASHBOARDS_INCLUDE_VALUES: set[ListDashboardsInclude] = {
    "panels",
}


def check_list_dashboards_include(value: str | None) -> ListDashboardsInclude | None:
    if value is None:
        return None
    if value in LIST_DASHBOARDS_INCLUDE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_DASHBOARDS_INCLUDE_VALUES!r}")
