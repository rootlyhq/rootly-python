from typing import Literal, cast

StatusPageComponentGroupResponseDataType = Literal["status_page_component_groups"]

STATUS_PAGE_COMPONENT_GROUP_RESPONSE_DATA_TYPE_VALUES: set[StatusPageComponentGroupResponseDataType] = {
    "status_page_component_groups",
}


def check_status_page_component_group_response_data_type(
    value: str | None,
) -> StatusPageComponentGroupResponseDataType | None:
    if value is None:
        return None
    if value in STATUS_PAGE_COMPONENT_GROUP_RESPONSE_DATA_TYPE_VALUES:
        return cast(StatusPageComponentGroupResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_COMPONENT_GROUP_RESPONSE_DATA_TYPE_VALUES!r}"
    )
