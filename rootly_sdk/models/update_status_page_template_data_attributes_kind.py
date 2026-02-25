from typing import Literal, cast

UpdateStatusPageTemplateDataAttributesKind = Literal["normal", "scheduled"]

UPDATE_STATUS_PAGE_TEMPLATE_DATA_ATTRIBUTES_KIND_VALUES: set[UpdateStatusPageTemplateDataAttributesKind] = {
    "normal",
    "scheduled",
}


def check_update_status_page_template_data_attributes_kind(value: str | None) -> UpdateStatusPageTemplateDataAttributesKind | None:
    if value is None:
        return None
    if value in UPDATE_STATUS_PAGE_TEMPLATE_DATA_ATTRIBUTES_KIND_VALUES:
        return cast(UpdateStatusPageTemplateDataAttributesKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_STATUS_PAGE_TEMPLATE_DATA_ATTRIBUTES_KIND_VALUES!r}"
    )
