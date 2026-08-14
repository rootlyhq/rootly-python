from typing import Literal, cast

NewStatusPageAnnouncementDataType = Literal["status_page_announcements"]

NEW_STATUS_PAGE_ANNOUNCEMENT_DATA_TYPE_VALUES: set[NewStatusPageAnnouncementDataType] = {
    "status_page_announcements",
}


def check_new_status_page_announcement_data_type(value: str | None) -> NewStatusPageAnnouncementDataType | None:
    if value is None:
        return None
    if value in NEW_STATUS_PAGE_ANNOUNCEMENT_DATA_TYPE_VALUES:
        return cast(NewStatusPageAnnouncementDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_STATUS_PAGE_ANNOUNCEMENT_DATA_TYPE_VALUES!r}")
