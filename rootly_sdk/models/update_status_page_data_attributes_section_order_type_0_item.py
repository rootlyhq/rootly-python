from typing import Literal, cast

UpdateStatusPageDataAttributesSectionOrderType0Item = Literal["incidents", "maintenance", "system_status"]

UPDATE_STATUS_PAGE_DATA_ATTRIBUTES_SECTION_ORDER_TYPE_0_ITEM_VALUES: set[
    UpdateStatusPageDataAttributesSectionOrderType0Item
] = {
    "incidents",
    "maintenance",
    "system_status",
}


def check_update_status_page_data_attributes_section_order_type_0_item(
    value: str | None,
) -> UpdateStatusPageDataAttributesSectionOrderType0Item | None:
    if value is None:
        return None
    if value in UPDATE_STATUS_PAGE_DATA_ATTRIBUTES_SECTION_ORDER_TYPE_0_ITEM_VALUES:
        return cast(UpdateStatusPageDataAttributesSectionOrderType0Item, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_STATUS_PAGE_DATA_ATTRIBUTES_SECTION_ORDER_TYPE_0_ITEM_VALUES!r}"
    )
