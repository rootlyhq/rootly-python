from typing import Literal

UpdateStatusPageTemplateDataAttributesUpdateStatus = Literal[
    "completed", "identified", "in_progress", "investigating", "monitoring", "resolved", "scheduled"
]

UPDATE_STATUS_PAGE_TEMPLATE_DATA_ATTRIBUTES_UPDATE_STATUS_VALUES: set[
    UpdateStatusPageTemplateDataAttributesUpdateStatus
] = {
    "completed",
    "identified",
    "in_progress",
    "investigating",
    "monitoring",
    "resolved",
    "scheduled",
}


def check_update_status_page_template_data_attributes_update_status(
    value: str | None,
) -> UpdateStatusPageTemplateDataAttributesUpdateStatus | None:
    if value is None:
        return None
    if value in UPDATE_STATUS_PAGE_TEMPLATE_DATA_ATTRIBUTES_UPDATE_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_STATUS_PAGE_TEMPLATE_DATA_ATTRIBUTES_UPDATE_STATUS_VALUES!r}"
    )
