from typing import Literal

NewStatusPageComponentDataType = Literal["status_page_components"]

NEW_STATUS_PAGE_COMPONENT_DATA_TYPE_VALUES: set[NewStatusPageComponentDataType] = {
    "status_page_components",
}


def check_new_status_page_component_data_type(value: str | None) -> NewStatusPageComponentDataType | None:
    if value is None:
        return None
    if value in NEW_STATUS_PAGE_COMPONENT_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_STATUS_PAGE_COMPONENT_DATA_TYPE_VALUES!r}")
