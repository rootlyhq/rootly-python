from typing import Literal, cast

LiveCallRouterResponseDataType = Literal["live_call_routers"]

LIVE_CALL_ROUTER_RESPONSE_DATA_TYPE_VALUES: set[LiveCallRouterResponseDataType] = {
    "live_call_routers",
}


def check_live_call_router_response_data_type(value: str | None) -> LiveCallRouterResponseDataType | None:
    if value is None:
        return None
    if value in LIVE_CALL_ROUTER_RESPONSE_DATA_TYPE_VALUES:
        return cast(LiveCallRouterResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIVE_CALL_ROUTER_RESPONSE_DATA_TYPE_VALUES!r}")
