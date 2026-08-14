from typing import Literal, cast

UpdateStatusPageComponentGroupDataType = Literal["status_page_component_groups"]

UPDATE_STATUS_PAGE_COMPONENT_GROUP_DATA_TYPE_VALUES: set[UpdateStatusPageComponentGroupDataType] = {
    "status_page_component_groups",
}


def check_update_status_page_component_group_data_type(
    value: str | None,
) -> UpdateStatusPageComponentGroupDataType | None:
    if value is None:
        return None
    if value in UPDATE_STATUS_PAGE_COMPONENT_GROUP_DATA_TYPE_VALUES:
        return cast(UpdateStatusPageComponentGroupDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_STATUS_PAGE_COMPONENT_GROUP_DATA_TYPE_VALUES!r}"
    )
