from typing import Literal, cast

NewStatusPageTemplateDataAttributesKind = Literal["normal", "scheduled"]

NEW_STATUS_PAGE_TEMPLATE_DATA_ATTRIBUTES_KIND_VALUES: set[NewStatusPageTemplateDataAttributesKind] = {
    "normal",
    "scheduled",
}


def check_new_status_page_template_data_attributes_kind(value: str | None) -> NewStatusPageTemplateDataAttributesKind | None:
    if value is None:
        return None
    if value in NEW_STATUS_PAGE_TEMPLATE_DATA_ATTRIBUTES_KIND_VALUES:
        return cast(NewStatusPageTemplateDataAttributesKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_STATUS_PAGE_TEMPLATE_DATA_ATTRIBUTES_KIND_VALUES!r}"
    )
