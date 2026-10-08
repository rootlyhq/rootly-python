from typing import Literal

DashboardColor = Literal["#D7F5E1", "#E9E2FF", "#FAE6E8", "#FAEEE6", "#FCF2CF"]

DASHBOARD_COLOR_VALUES: set[DashboardColor] = {
    "#D7F5E1",
    "#E9E2FF",
    "#FAE6E8",
    "#FAEEE6",
    "#FCF2CF",
}


def check_dashboard_color(value: str | None) -> DashboardColor | None:
    if value is None:
        return None
    if value in DASHBOARD_COLOR_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DASHBOARD_COLOR_VALUES!r}")
