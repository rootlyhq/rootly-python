from typing import Literal, cast

AlertRouteResponseDataType = Literal["alert_routes"]

ALERT_ROUTE_RESPONSE_DATA_TYPE_VALUES: set[AlertRouteResponseDataType] = {
    "alert_routes",
}


def check_alert_route_response_data_type(value: str | None) -> AlertRouteResponseDataType | None:
    if value is None:
        return None
    if value in ALERT_ROUTE_RESPONSE_DATA_TYPE_VALUES:
        return cast(AlertRouteResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_ROUTE_RESPONSE_DATA_TYPE_VALUES!r}")
