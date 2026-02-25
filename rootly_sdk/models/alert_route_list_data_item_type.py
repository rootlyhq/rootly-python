from typing import Literal, cast

AlertRouteListDataItemType = Literal["alert_routes"]

ALERT_ROUTE_LIST_DATA_ITEM_TYPE_VALUES: set[AlertRouteListDataItemType] = {
    "alert_routes",
}


def check_alert_route_list_data_item_type(value: str | None) -> AlertRouteListDataItemType | None:
    if value is None:
        return None
    if value in ALERT_ROUTE_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(AlertRouteListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_ROUTE_LIST_DATA_ITEM_TYPE_VALUES!r}")
