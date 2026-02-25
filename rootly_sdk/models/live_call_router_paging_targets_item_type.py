from typing import Literal, cast

LiveCallRouterPagingTargetsItemType = Literal["escalation_policy", "service", "team"]

LIVE_CALL_ROUTER_PAGING_TARGETS_ITEM_TYPE_VALUES: set[LiveCallRouterPagingTargetsItemType] = {
    "escalation_policy",
    "service",
    "team",
}


def check_live_call_router_paging_targets_item_type(value: str | None) -> LiveCallRouterPagingTargetsItemType | None:
    if value is None:
        return None
    if value in LIVE_CALL_ROUTER_PAGING_TARGETS_ITEM_TYPE_VALUES:
        return cast(LiveCallRouterPagingTargetsItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIVE_CALL_ROUTER_PAGING_TARGETS_ITEM_TYPE_VALUES!r}")
