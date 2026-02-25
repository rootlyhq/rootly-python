from typing import Literal, cast

DashboardPanelParamsDisplay = Literal[
    "aggregate_value",
    "column_chart",
    "line_chart",
    "line_stepped_chart",
    "monitoring_chart",
    "pie_chart",
    "stacked_column_chart",
    "table",
]

DASHBOARD_PANEL_PARAMS_DISPLAY_VALUES: set[DashboardPanelParamsDisplay] = {
    "aggregate_value",
    "column_chart",
    "line_chart",
    "line_stepped_chart",
    "monitoring_chart",
    "pie_chart",
    "stacked_column_chart",
    "table",
}


def check_dashboard_panel_params_display(value: str | None) -> DashboardPanelParamsDisplay | None:
    if value is None:
        return None
    if value in DASHBOARD_PANEL_PARAMS_DISPLAY_VALUES:
        return cast(DashboardPanelParamsDisplay, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DASHBOARD_PANEL_PARAMS_DISPLAY_VALUES!r}")
