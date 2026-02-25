from typing import Literal, cast

StatusPageTemplateResponseDataType = Literal["status_page_templates"]

STATUS_PAGE_TEMPLATE_RESPONSE_DATA_TYPE_VALUES: set[StatusPageTemplateResponseDataType] = {
    "status_page_templates",
}


def check_status_page_template_response_data_type(value: str | None) -> StatusPageTemplateResponseDataType | None:
    if value is None:
        return None
    if value in STATUS_PAGE_TEMPLATE_RESPONSE_DATA_TYPE_VALUES:
        return cast(StatusPageTemplateResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_TEMPLATE_RESPONSE_DATA_TYPE_VALUES!r}")
