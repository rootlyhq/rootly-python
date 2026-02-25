from typing import Literal, cast

UpdateLiveCallRouterDataAttributesKind = Literal["live", "voicemail"]

UPDATE_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_KIND_VALUES: set[UpdateLiveCallRouterDataAttributesKind] = {
    "live",
    "voicemail",
}


def check_update_live_call_router_data_attributes_kind(value: str | None) -> UpdateLiveCallRouterDataAttributesKind | None:
    if value is None:
        return None
    if value in UPDATE_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_KIND_VALUES:
        return cast(UpdateLiveCallRouterDataAttributesKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_KIND_VALUES!r}"
    )
