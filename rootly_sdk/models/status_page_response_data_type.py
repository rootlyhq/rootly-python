from typing import Literal, cast

StatusPageResponseDataType = Literal["status_pages"]

STATUS_PAGE_RESPONSE_DATA_TYPE_VALUES: set[StatusPageResponseDataType] = {
    "status_pages",
}


def check_status_page_response_data_type(value: str | None) -> StatusPageResponseDataType | None:
    if value is None:
        return None
    if value in STATUS_PAGE_RESPONSE_DATA_TYPE_VALUES:
        return cast(StatusPageResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_RESPONSE_DATA_TYPE_VALUES!r}")
