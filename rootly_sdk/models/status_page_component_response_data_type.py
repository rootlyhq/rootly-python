from typing import Literal, cast

StatusPageComponentResponseDataType = Literal["status_page_components"]

STATUS_PAGE_COMPONENT_RESPONSE_DATA_TYPE_VALUES: set[StatusPageComponentResponseDataType] = {
    "status_page_components",
}


def check_status_page_component_response_data_type(value: str | None) -> StatusPageComponentResponseDataType | None:
    if value is None:
        return None
    if value in STATUS_PAGE_COMPONENT_RESPONSE_DATA_TYPE_VALUES:
        return cast(StatusPageComponentResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_COMPONENT_RESPONSE_DATA_TYPE_VALUES!r}")
