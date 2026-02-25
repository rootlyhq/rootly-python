from typing import Literal, cast

NewStatusPageTemplateDataType = Literal["status_page_templates"]

NEW_STATUS_PAGE_TEMPLATE_DATA_TYPE_VALUES: set[NewStatusPageTemplateDataType] = {
    "status_page_templates",
}


def check_new_status_page_template_data_type(value: str | None) -> NewStatusPageTemplateDataType | None:
    if value is None:
        return None
    if value in NEW_STATUS_PAGE_TEMPLATE_DATA_TYPE_VALUES:
        return cast(NewStatusPageTemplateDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_STATUS_PAGE_TEMPLATE_DATA_TYPE_VALUES!r}")
