from typing import Literal, cast

NewLiveCallRouterDataAttributesPagingTargetsItemType = Literal["escalation_policy", "service", "team"]

NEW_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_PAGING_TARGETS_ITEM_TYPE_VALUES: set[
    NewLiveCallRouterDataAttributesPagingTargetsItemType
] = {
    "escalation_policy",
    "service",
    "team",
}


def check_new_live_call_router_data_attributes_paging_targets_item_type(
    value: str | None,
) -> NewLiveCallRouterDataAttributesPagingTargetsItemType | None:
    if value is None:
        return None
    if value in NEW_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_PAGING_TARGETS_ITEM_TYPE_VALUES:
        return cast(NewLiveCallRouterDataAttributesPagingTargetsItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_PAGING_TARGETS_ITEM_TYPE_VALUES!r}"
    )
