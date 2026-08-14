from typing import Literal, cast

NewStatusPageComponentDataAttributesSourceType = Literal["Functionality", "Service"]

NEW_STATUS_PAGE_COMPONENT_DATA_ATTRIBUTES_SOURCE_TYPE_VALUES: set[NewStatusPageComponentDataAttributesSourceType] = {
    "Functionality",
    "Service",
}


def check_new_status_page_component_data_attributes_source_type(
    value: str | None,
) -> NewStatusPageComponentDataAttributesSourceType | None:
    if value is None:
        return None
    if value in NEW_STATUS_PAGE_COMPONENT_DATA_ATTRIBUTES_SOURCE_TYPE_VALUES:
        return cast(NewStatusPageComponentDataAttributesSourceType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_STATUS_PAGE_COMPONENT_DATA_ATTRIBUTES_SOURCE_TYPE_VALUES!r}"
    )
