from typing import Literal, cast

UpdateLiveCallRouterDataType = Literal["live_call_routers"]

UPDATE_LIVE_CALL_ROUTER_DATA_TYPE_VALUES: set[UpdateLiveCallRouterDataType] = {
    "live_call_routers",
}


def check_update_live_call_router_data_type(value: str | None) -> UpdateLiveCallRouterDataType | None:
    if value is None:
        return None
    if value in UPDATE_LIVE_CALL_ROUTER_DATA_TYPE_VALUES:
        return cast(UpdateLiveCallRouterDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_LIVE_CALL_ROUTER_DATA_TYPE_VALUES!r}")
