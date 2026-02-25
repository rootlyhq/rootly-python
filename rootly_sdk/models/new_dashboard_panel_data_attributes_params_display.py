from typing import Literal, cast

NewDashboardPanelDataAttributesParamsDisplay = Literal[
    "aggregate_value",
    "column_chart",
    "line_chart",
    "line_stepped_chart",
    "monitoring_chart",
    "pie_chart",
    "stacked_column_chart",
    "table",
]

NEW_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DISPLAY_VALUES: set[NewDashboardPanelDataAttributesParamsDisplay] = {
    "aggregate_value",
    "column_chart",
    "line_chart",
    "line_stepped_chart",
    "monitoring_chart",
    "pie_chart",
    "stacked_column_chart",
    "table",
}


def check_new_dashboard_panel_data_attributes_params_display(
    value: str | None,
) -> NewDashboardPanelDataAttributesParamsDisplay | None:
    if value is None:
        return None
    if value in NEW_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DISPLAY_VALUES:
        return cast(NewDashboardPanelDataAttributesParamsDisplay, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DISPLAY_VALUES!r}"
    )
