from typing import Literal, cast

DashboardPanelListDataItemType = Literal["dashboard_panels"]

DASHBOARD_PANEL_LIST_DATA_ITEM_TYPE_VALUES: set[DashboardPanelListDataItemType] = {
    "dashboard_panels",
}


def check_dashboard_panel_list_data_item_type(value: str | None) -> DashboardPanelListDataItemType | None:
    if value is None:
        return None
    if value in DASHBOARD_PANEL_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(DashboardPanelListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DASHBOARD_PANEL_LIST_DATA_ITEM_TYPE_VALUES!r}")
