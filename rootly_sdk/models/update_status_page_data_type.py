from typing import Literal, cast

UpdateStatusPageDataType = Literal["status_pages"]

UPDATE_STATUS_PAGE_DATA_TYPE_VALUES: set[UpdateStatusPageDataType] = {
    "status_pages",
}


def check_update_status_page_data_type(value: str | None) -> UpdateStatusPageDataType | None:
    if value is None:
        return None
    if value in UPDATE_STATUS_PAGE_DATA_TYPE_VALUES:
        return cast(UpdateStatusPageDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_STATUS_PAGE_DATA_TYPE_VALUES!r}")
