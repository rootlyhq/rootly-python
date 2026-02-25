from typing import Literal, cast

UpdateStatusPageTemplateDataType = Literal["status_page_templates"]

UPDATE_STATUS_PAGE_TEMPLATE_DATA_TYPE_VALUES: set[UpdateStatusPageTemplateDataType] = {
    "status_page_templates",
}


def check_update_status_page_template_data_type(value: str | None) -> UpdateStatusPageTemplateDataType | None:
    if value is None:
        return None
    if value in UPDATE_STATUS_PAGE_TEMPLATE_DATA_TYPE_VALUES:
        return cast(UpdateStatusPageTemplateDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_STATUS_PAGE_TEMPLATE_DATA_TYPE_VALUES!r}")
