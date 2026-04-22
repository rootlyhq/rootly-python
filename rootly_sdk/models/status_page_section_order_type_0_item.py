from typing import Literal, cast

StatusPageSectionOrderType0Item = Literal["incidents", "maintenance", "system_status"]

STATUS_PAGE_SECTION_ORDER_TYPE_0_ITEM_VALUES: set[StatusPageSectionOrderType0Item] = {
    "incidents",
    "maintenance",
    "system_status",
}


def check_status_page_section_order_type_0_item(value: str | None) -> StatusPageSectionOrderType0Item | None:
    if value is None:
        return None
    if value in STATUS_PAGE_SECTION_ORDER_TYPE_0_ITEM_VALUES:
        return cast(StatusPageSectionOrderType0Item, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_SECTION_ORDER_TYPE_0_ITEM_VALUES!r}")
