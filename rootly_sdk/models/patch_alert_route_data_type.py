from typing import Literal, cast

PatchAlertRouteDataType = Literal["alert_routes"]

PATCH_ALERT_ROUTE_DATA_TYPE_VALUES: set[PatchAlertRouteDataType] = {
    "alert_routes",
}


def check_patch_alert_route_data_type(value: str | None) -> PatchAlertRouteDataType | None:
    if value is None:
        return None
    if value in PATCH_ALERT_ROUTE_DATA_TYPE_VALUES:
        return cast(PatchAlertRouteDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCH_ALERT_ROUTE_DATA_TYPE_VALUES!r}")
