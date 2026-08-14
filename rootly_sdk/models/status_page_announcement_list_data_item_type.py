from typing import Literal, cast

StatusPageAnnouncementListDataItemType = Literal["status_page_announcements"]

STATUS_PAGE_ANNOUNCEMENT_LIST_DATA_ITEM_TYPE_VALUES: set[StatusPageAnnouncementListDataItemType] = {
    "status_page_announcements",
}


def check_status_page_announcement_list_data_item_type(
    value: str | None,
) -> StatusPageAnnouncementListDataItemType | None:
    if value is None:
        return None
    if value in STATUS_PAGE_ANNOUNCEMENT_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(StatusPageAnnouncementListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_ANNOUNCEMENT_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
