from typing import Literal, cast

OnCallShadowsListDataItemType = Literal["on_call_shadows"]

ON_CALL_SHADOWS_LIST_DATA_ITEM_TYPE_VALUES: set[OnCallShadowsListDataItemType] = {
    "on_call_shadows",
}


def check_on_call_shadows_list_data_item_type(value: str | None) -> OnCallShadowsListDataItemType | None:
    if value is None:
        return None
    if value in ON_CALL_SHADOWS_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(OnCallShadowsListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_SHADOWS_LIST_DATA_ITEM_TYPE_VALUES!r}")
