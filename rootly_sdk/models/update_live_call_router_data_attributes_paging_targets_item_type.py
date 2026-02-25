from typing import Literal, cast

UpdateLiveCallRouterDataAttributesPagingTargetsItemType = Literal["escalation_policy", "service", "team"]

UPDATE_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_PAGING_TARGETS_ITEM_TYPE_VALUES: set[
    UpdateLiveCallRouterDataAttributesPagingTargetsItemType
] = {
    "escalation_policy",
    "service",
    "team",
}


def check_update_live_call_router_data_attributes_paging_targets_item_type(
    value: str | None,
) -> UpdateLiveCallRouterDataAttributesPagingTargetsItemType | None:
    if value is None:
        return None
    if value in UPDATE_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_PAGING_TARGETS_ITEM_TYPE_VALUES:
        return cast(UpdateLiveCallRouterDataAttributesPagingTargetsItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_PAGING_TARGETS_ITEM_TYPE_VALUES!r}"
    )
