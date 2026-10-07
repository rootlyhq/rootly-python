from typing import Literal

NewAlertRouteDataType = Literal["alert_routes"]

NEW_ALERT_ROUTE_DATA_TYPE_VALUES: set[NewAlertRouteDataType] = {
    "alert_routes",
}


def check_new_alert_route_data_type(value: str | None) -> NewAlertRouteDataType | None:
    if value is None:
        return None
    if value in NEW_ALERT_ROUTE_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_ALERT_ROUTE_DATA_TYPE_VALUES!r}")
