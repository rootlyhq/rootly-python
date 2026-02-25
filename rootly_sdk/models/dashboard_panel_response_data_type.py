from typing import Literal, cast

DashboardPanelResponseDataType = Literal["dashboard_panels"]

DASHBOARD_PANEL_RESPONSE_DATA_TYPE_VALUES: set[DashboardPanelResponseDataType] = {
    "dashboard_panels",
}


def check_dashboard_panel_response_data_type(value: str | None) -> DashboardPanelResponseDataType | None:
    if value is None:
        return None
    if value in DASHBOARD_PANEL_RESPONSE_DATA_TYPE_VALUES:
        return cast(DashboardPanelResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DASHBOARD_PANEL_RESPONSE_DATA_TYPE_VALUES!r}")
