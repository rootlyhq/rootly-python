from typing import Literal, cast

CatalogChecklistTemplateFieldsType0ItemFieldSource = Literal["builtin", "custom"]

CATALOG_CHECKLIST_TEMPLATE_FIELDS_TYPE_0_ITEM_FIELD_SOURCE_VALUES: set[
    CatalogChecklistTemplateFieldsType0ItemFieldSource
] = {
    "builtin",
    "custom",
}


def check_catalog_checklist_template_fields_type_0_item_field_source(
    value: str | None,
) -> CatalogChecklistTemplateFieldsType0ItemFieldSource | None:
    if value is None:
        return None
    if value in CATALOG_CHECKLIST_TEMPLATE_FIELDS_TYPE_0_ITEM_FIELD_SOURCE_VALUES:
        return cast(CatalogChecklistTemplateFieldsType0ItemFieldSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOG_CHECKLIST_TEMPLATE_FIELDS_TYPE_0_ITEM_FIELD_SOURCE_VALUES!r}"
    )
