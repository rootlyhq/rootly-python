from typing import Literal, cast

DashboardListDataItemType = Literal["dashboards"]

DASHBOARD_LIST_DATA_ITEM_TYPE_VALUES: set[DashboardListDataItemType] = {
    "dashboards",
}


def check_dashboard_list_data_item_type(value: str | None) -> DashboardListDataItemType | None:
    if value is None:
        return None
    if value in DASHBOARD_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(DashboardListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DASHBOARD_LIST_DATA_ITEM_TYPE_VALUES!r}")
