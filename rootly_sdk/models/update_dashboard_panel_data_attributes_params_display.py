from typing import Literal, cast

UpdateDashboardPanelDataAttributesParamsDisplay = Literal[
    "aggregate_value",
    "column_chart",
    "line_chart",
    "line_stepped_chart",
    "monitoring_chart",
    "pie_chart",
    "stacked_column_chart",
    "table",
]

UPDATE_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DISPLAY_VALUES: set[UpdateDashboardPanelDataAttributesParamsDisplay] = {
    "aggregate_value",
    "column_chart",
    "line_chart",
    "line_stepped_chart",
    "monitoring_chart",
    "pie_chart",
    "stacked_column_chart",
    "table",
}


def check_update_dashboard_panel_data_attributes_params_display(
    value: str | None,
) -> UpdateDashboardPanelDataAttributesParamsDisplay | None:
    if value is None:
        return None
    if value in UPDATE_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DISPLAY_VALUES:
        return cast(UpdateDashboardPanelDataAttributesParamsDisplay, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DISPLAY_VALUES!r}"
    )
