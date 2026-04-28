from typing import Literal, cast

NewCatalogChecklistTemplateDataAttributesCustomFieldFieldSource = Literal["custom"]

NEW_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_CUSTOM_FIELD_FIELD_SOURCE_VALUES: set[
    NewCatalogChecklistTemplateDataAttributesCustomFieldFieldSource
] = {
    "custom",
}


def check_new_catalog_checklist_template_data_attributes_custom_field_field_source(
    value: str | None,
) -> NewCatalogChecklistTemplateDataAttributesCustomFieldFieldSource | None:
    if value is None:
        return None
    if value in NEW_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_CUSTOM_FIELD_FIELD_SOURCE_VALUES:
        return cast(NewCatalogChecklistTemplateDataAttributesCustomFieldFieldSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_CUSTOM_FIELD_FIELD_SOURCE_VALUES!r}"
    )
