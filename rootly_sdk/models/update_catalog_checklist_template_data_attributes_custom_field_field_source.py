from typing import Literal, cast

UpdateCatalogChecklistTemplateDataAttributesCustomFieldFieldSource = Literal["custom"]

UPDATE_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_CUSTOM_FIELD_FIELD_SOURCE_VALUES: set[
    UpdateCatalogChecklistTemplateDataAttributesCustomFieldFieldSource
] = {
    "custom",
}


def check_update_catalog_checklist_template_data_attributes_custom_field_field_source(
    value: str | None,
) -> UpdateCatalogChecklistTemplateDataAttributesCustomFieldFieldSource | None:
    if value is None:
        return None
    if value in UPDATE_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_CUSTOM_FIELD_FIELD_SOURCE_VALUES:
        return cast(UpdateCatalogChecklistTemplateDataAttributesCustomFieldFieldSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_CUSTOM_FIELD_FIELD_SOURCE_VALUES!r}"
    )
