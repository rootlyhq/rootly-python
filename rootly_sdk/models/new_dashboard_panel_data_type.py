from typing import Literal, cast

NewDashboardPanelDataType = Literal["dashboard_panels"]

NEW_DASHBOARD_PANEL_DATA_TYPE_VALUES: set[NewDashboardPanelDataType] = {
    "dashboard_panels",
}


def check_new_dashboard_panel_data_type(value: str | None) -> NewDashboardPanelDataType | None:
    if value is None:
        return None
    if value in NEW_DASHBOARD_PANEL_DATA_TYPE_VALUES:
        return cast(NewDashboardPanelDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_DASHBOARD_PANEL_DATA_TYPE_VALUES!r}")
