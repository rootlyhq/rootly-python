from typing import Literal, cast

LiveCallRouterListDataItemType = Literal["live_call_routers"]

LIVE_CALL_ROUTER_LIST_DATA_ITEM_TYPE_VALUES: set[LiveCallRouterListDataItemType] = {
    "live_call_routers",
}


def check_live_call_router_list_data_item_type(value: str | None) -> LiveCallRouterListDataItemType | None:
    if value is None:
        return None
    if value in LIVE_CALL_ROUTER_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(LiveCallRouterListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIVE_CALL_ROUTER_LIST_DATA_ITEM_TYPE_VALUES!r}")
