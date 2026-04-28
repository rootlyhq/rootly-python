from typing import Literal, cast

NewStatusPageDataAttributesSectionOrderType0Item = Literal["incidents", "maintenance", "system_status"]

NEW_STATUS_PAGE_DATA_ATTRIBUTES_SECTION_ORDER_TYPE_0_ITEM_VALUES: set[
    NewStatusPageDataAttributesSectionOrderType0Item
] = {
    "incidents",
    "maintenance",
    "system_status",
}


def check_new_status_page_data_attributes_section_order_type_0_item(
    value: str | None,
) -> NewStatusPageDataAttributesSectionOrderType0Item | None:
    if value is None:
        return None
    if value in NEW_STATUS_PAGE_DATA_ATTRIBUTES_SECTION_ORDER_TYPE_0_ITEM_VALUES:
        return cast(NewStatusPageDataAttributesSectionOrderType0Item, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_STATUS_PAGE_DATA_ATTRIBUTES_SECTION_ORDER_TYPE_0_ITEM_VALUES!r}"
    )
