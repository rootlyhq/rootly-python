from typing import Literal, cast

StatusPageAnnouncementResponseDataType = Literal["status_page_announcements"]

STATUS_PAGE_ANNOUNCEMENT_RESPONSE_DATA_TYPE_VALUES: set[StatusPageAnnouncementResponseDataType] = {
    "status_page_announcements",
}


def check_status_page_announcement_response_data_type(
    value: str | None,
) -> StatusPageAnnouncementResponseDataType | None:
    if value is None:
        return None
    if value in STATUS_PAGE_ANNOUNCEMENT_RESPONSE_DATA_TYPE_VALUES:
        return cast(StatusPageAnnouncementResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_ANNOUNCEMENT_RESPONSE_DATA_TYPE_VALUES!r}"
    )
