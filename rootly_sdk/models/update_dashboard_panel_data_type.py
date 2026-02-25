from typing import Literal, cast

UpdateDashboardPanelDataType = Literal["dashboard_panels"]

UPDATE_DASHBOARD_PANEL_DATA_TYPE_VALUES: set[UpdateDashboardPanelDataType] = {
    "dashboard_panels",
}


def check_update_dashboard_panel_data_type(value: str | None) -> UpdateDashboardPanelDataType | None:
    if value is None:
        return None
    if value in UPDATE_DASHBOARD_PANEL_DATA_TYPE_VALUES:
        return cast(UpdateDashboardPanelDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_DASHBOARD_PANEL_DATA_TYPE_VALUES!r}")
