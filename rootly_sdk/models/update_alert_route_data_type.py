from typing import Literal, cast

UpdateAlertRouteDataType = Literal["alert_routes"]

UPDATE_ALERT_ROUTE_DATA_TYPE_VALUES: set[UpdateAlertRouteDataType] = {
    "alert_routes",
}


def check_update_alert_route_data_type(value: str | None) -> UpdateAlertRouteDataType | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_ROUTE_DATA_TYPE_VALUES:
        return cast(UpdateAlertRouteDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_ROUTE_DATA_TYPE_VALUES!r}")
