from typing import Literal, cast

NewCatalogChecklistTemplateDataAttributesCatalogType = Literal[
    "Catalog", "Cause", "Environment", "Functionality", "Group", "IncidentType", "Service"
]

NEW_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_CATALOG_TYPE_VALUES: set[
    NewCatalogChecklistTemplateDataAttributesCatalogType
] = {
    "Catalog",
    "Cause",
    "Environment",
    "Functionality",
    "Group",
    "IncidentType",
    "Service",
}


def check_new_catalog_checklist_template_data_attributes_catalog_type(
    value: str | None,
) -> NewCatalogChecklistTemplateDataAttributesCatalogType | None:
    if value is None:
        return None
    if value in NEW_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_CATALOG_TYPE_VALUES:
        return cast(NewCatalogChecklistTemplateDataAttributesCatalogType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_CATALOG_TYPE_VALUES!r}"
    )
