from typing import Literal, cast

NewCatalogChecklistTemplateDataAttributesBuiltinFieldFieldSource = Literal["builtin"]

NEW_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_BUILTIN_FIELD_FIELD_SOURCE_VALUES: set[
    NewCatalogChecklistTemplateDataAttributesBuiltinFieldFieldSource
] = {
    "builtin",
}


def check_new_catalog_checklist_template_data_attributes_builtin_field_field_source(
    value: str | None,
) -> NewCatalogChecklistTemplateDataAttributesBuiltinFieldFieldSource | None:
    if value is None:
        return None
    if value in NEW_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_BUILTIN_FIELD_FIELD_SOURCE_VALUES:
        return cast(NewCatalogChecklistTemplateDataAttributesBuiltinFieldFieldSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_BUILTIN_FIELD_FIELD_SOURCE_VALUES!r}"
    )
