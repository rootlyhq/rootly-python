from typing import Literal

UpdateStatusPageAnnouncementDataType = Literal["status_page_announcements"]

UPDATE_STATUS_PAGE_ANNOUNCEMENT_DATA_TYPE_VALUES: set[UpdateStatusPageAnnouncementDataType] = {
    "status_page_announcements",
}


def check_update_status_page_announcement_data_type(value: str | None) -> UpdateStatusPageAnnouncementDataType | None:
    if value is None:
        return None
    if value in UPDATE_STATUS_PAGE_ANNOUNCEMENT_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_STATUS_PAGE_ANNOUNCEMENT_DATA_TYPE_VALUES!r}")
