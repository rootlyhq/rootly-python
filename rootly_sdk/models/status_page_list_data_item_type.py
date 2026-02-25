from typing import Literal, cast

StatusPageListDataItemType = Literal["status_pages"]

STATUS_PAGE_LIST_DATA_ITEM_TYPE_VALUES: set[StatusPageListDataItemType] = {
    "status_pages",
}


def check_status_page_list_data_item_type(value: str | None) -> StatusPageListDataItemType | None:
    if value is None:
        return None
    if value in STATUS_PAGE_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(StatusPageListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_LIST_DATA_ITEM_TYPE_VALUES!r}")
