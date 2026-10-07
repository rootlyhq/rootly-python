from typing import Literal

UpdateStatusPageComponentDataType = Literal["status_page_components"]

UPDATE_STATUS_PAGE_COMPONENT_DATA_TYPE_VALUES: set[UpdateStatusPageComponentDataType] = {
    "status_page_components",
}


def check_update_status_page_component_data_type(value: str | None) -> UpdateStatusPageComponentDataType | None:
    if value is None:
        return None
    if value in UPDATE_STATUS_PAGE_COMPONENT_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_STATUS_PAGE_COMPONENT_DATA_TYPE_VALUES!r}")
