from typing import Literal, cast

StatusPageComponentGroupListDataItemType = Literal["status_page_component_groups"]

STATUS_PAGE_COMPONENT_GROUP_LIST_DATA_ITEM_TYPE_VALUES: set[StatusPageComponentGroupListDataItemType] = {
    "status_page_component_groups",
}


def check_status_page_component_group_list_data_item_type(
    value: str | None,
) -> StatusPageComponentGroupListDataItemType | None:
    if value is None:
        return None
    if value in STATUS_PAGE_COMPONENT_GROUP_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(StatusPageComponentGroupListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_COMPONENT_GROUP_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
