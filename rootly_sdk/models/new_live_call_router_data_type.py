from typing import Literal, cast

NewLiveCallRouterDataType = Literal["live_call_routers"]

NEW_LIVE_CALL_ROUTER_DATA_TYPE_VALUES: set[NewLiveCallRouterDataType] = {
    "live_call_routers",
}


def check_new_live_call_router_data_type(value: str | None) -> NewLiveCallRouterDataType | None:
    if value is None:
        return None
    if value in NEW_LIVE_CALL_ROUTER_DATA_TYPE_VALUES:
        return cast(NewLiveCallRouterDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_LIVE_CALL_ROUTER_DATA_TYPE_VALUES!r}")
