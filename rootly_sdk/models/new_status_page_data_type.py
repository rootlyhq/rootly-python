from typing import Literal, cast

NewStatusPageDataType = Literal["status_pages"]

NEW_STATUS_PAGE_DATA_TYPE_VALUES: set[NewStatusPageDataType] = {
    "status_pages",
}


def check_new_status_page_data_type(value: str | None) -> NewStatusPageDataType | None:
    if value is None:
        return None
    if value in NEW_STATUS_PAGE_DATA_TYPE_VALUES:
        return cast(NewStatusPageDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_STATUS_PAGE_DATA_TYPE_VALUES!r}")
