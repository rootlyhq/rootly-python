from typing import Literal, cast

LiveCallRouterPhoneType = Literal["local", "mobile", "toll_free"]

LIVE_CALL_ROUTER_PHONE_TYPE_VALUES: set[LiveCallRouterPhoneType] = {
    "local",
    "mobile",
    "toll_free",
}


def check_live_call_router_phone_type(value: str | None) -> LiveCallRouterPhoneType | None:
    if value is None:
        return None
    if value in LIVE_CALL_ROUTER_PHONE_TYPE_VALUES:
        return cast(LiveCallRouterPhoneType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIVE_CALL_ROUTER_PHONE_TYPE_VALUES!r}")
