from typing import Literal

NewStatusPageComponentGroupDataType = Literal["status_page_component_groups"]

NEW_STATUS_PAGE_COMPONENT_GROUP_DATA_TYPE_VALUES: set[NewStatusPageComponentGroupDataType] = {
    "status_page_component_groups",
}


def check_new_status_page_component_group_data_type(value: str | None) -> NewStatusPageComponentGroupDataType | None:
    if value is None:
        return None
    if value in NEW_STATUS_PAGE_COMPONENT_GROUP_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_STATUS_PAGE_COMPONENT_GROUP_DATA_TYPE_VALUES!r}")
