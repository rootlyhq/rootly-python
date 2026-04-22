from typing import Literal, cast

CatalogChecklistTemplateCatalogType = Literal[
    "Catalog", "Cause", "Environment", "Functionality", "Group", "IncidentType", "Service"
]

CATALOG_CHECKLIST_TEMPLATE_CATALOG_TYPE_VALUES: set[CatalogChecklistTemplateCatalogType] = {
    "Catalog",
    "Cause",
    "Environment",
    "Functionality",
    "Group",
    "IncidentType",
    "Service",
}


def check_catalog_checklist_template_catalog_type(value: str | None) -> CatalogChecklistTemplateCatalogType | None:
    if value is None:
        return None
    if value in CATALOG_CHECKLIST_TEMPLATE_CATALOG_TYPE_VALUES:
        return cast(CatalogChecklistTemplateCatalogType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOG_CHECKLIST_TEMPLATE_CATALOG_TYPE_VALUES!r}")
