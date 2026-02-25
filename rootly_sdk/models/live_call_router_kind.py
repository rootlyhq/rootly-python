from typing import Literal, cast

LiveCallRouterKind = Literal["live", "voicemail"]

LIVE_CALL_ROUTER_KIND_VALUES: set[LiveCallRouterKind] = {
    "live",
    "voicemail",
}


def check_live_call_router_kind(value: str | None) -> LiveCallRouterKind | None:
    if value is None:
        return None
    if value in LIVE_CALL_ROUTER_KIND_VALUES:
        return cast(LiveCallRouterKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIVE_CALL_ROUTER_KIND_VALUES!r}")
