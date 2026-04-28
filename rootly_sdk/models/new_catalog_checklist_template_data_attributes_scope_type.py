from typing import Literal, cast

NewCatalogChecklistTemplateDataAttributesScopeType = Literal["Catalog", "Team"]

NEW_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_SCOPE_TYPE_VALUES: set[
    NewCatalogChecklistTemplateDataAttributesScopeType
] = {
    "Catalog",
    "Team",
}


def check_new_catalog_checklist_template_data_attributes_scope_type(
    value: str | None,
) -> NewCatalogChecklistTemplateDataAttributesScopeType | None:
    if value is None:
        return None
    if value in NEW_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_SCOPE_TYPE_VALUES:
        return cast(NewCatalogChecklistTemplateDataAttributesScopeType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_SCOPE_TYPE_VALUES!r}"
    )
