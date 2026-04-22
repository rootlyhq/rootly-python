from typing import Literal, cast

UpdateCatalogChecklistTemplateDataAttributesBuiltinFieldFieldSource = Literal["builtin"]

UPDATE_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_BUILTIN_FIELD_FIELD_SOURCE_VALUES: set[
    UpdateCatalogChecklistTemplateDataAttributesBuiltinFieldFieldSource
] = {
    "builtin",
}


def check_update_catalog_checklist_template_data_attributes_builtin_field_field_source(
    value: str | None,
) -> UpdateCatalogChecklistTemplateDataAttributesBuiltinFieldFieldSource | None:
    if value is None:
        return None
    if value in UPDATE_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_BUILTIN_FIELD_FIELD_SOURCE_VALUES:
        return cast(UpdateCatalogChecklistTemplateDataAttributesBuiltinFieldFieldSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_BUILTIN_FIELD_FIELD_SOURCE_VALUES!r}"
    )
