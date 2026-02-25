from typing import Literal, cast

StatusPageTemplateListDataItemType = Literal["status_page_templates"]

STATUS_PAGE_TEMPLATE_LIST_DATA_ITEM_TYPE_VALUES: set[StatusPageTemplateListDataItemType] = {
    "status_page_templates",
}


def check_status_page_template_list_data_item_type(value: str | None) -> StatusPageTemplateListDataItemType | None:
    if value is None:
        return None
    if value in STATUS_PAGE_TEMPLATE_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(StatusPageTemplateListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_TEMPLATE_LIST_DATA_ITEM_TYPE_VALUES!r}")
