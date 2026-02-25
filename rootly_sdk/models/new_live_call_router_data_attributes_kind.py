from typing import Literal, cast

NewLiveCallRouterDataAttributesKind = Literal["live", "voicemail"]

NEW_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_KIND_VALUES: set[NewLiveCallRouterDataAttributesKind] = {
    "live",
    "voicemail",
}


def check_new_live_call_router_data_attributes_kind(value: str | None) -> NewLiveCallRouterDataAttributesKind | None:
    if value is None:
        return None
    if value in NEW_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_KIND_VALUES:
        return cast(NewLiveCallRouterDataAttributesKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_KIND_VALUES!r}")
