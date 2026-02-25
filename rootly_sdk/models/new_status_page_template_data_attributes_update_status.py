from typing import Literal, cast

NewStatusPageTemplateDataAttributesUpdateStatus = Literal[
    "completed", "identified", "in_progress", "investigating", "monitoring", "resolved", "scheduled"
]

NEW_STATUS_PAGE_TEMPLATE_DATA_ATTRIBUTES_UPDATE_STATUS_VALUES: set[NewStatusPageTemplateDataAttributesUpdateStatus] = {
    "completed",
    "identified",
    "in_progress",
    "investigating",
    "monitoring",
    "resolved",
    "scheduled",
}


def check_new_status_page_template_data_attributes_update_status(
    value: str | None,
) -> NewStatusPageTemplateDataAttributesUpdateStatus | None:
    if value is None:
        return None
    if value in NEW_STATUS_PAGE_TEMPLATE_DATA_ATTRIBUTES_UPDATE_STATUS_VALUES:
        return cast(NewStatusPageTemplateDataAttributesUpdateStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_STATUS_PAGE_TEMPLATE_DATA_ATTRIBUTES_UPDATE_STATUS_VALUES!r}"
    )
