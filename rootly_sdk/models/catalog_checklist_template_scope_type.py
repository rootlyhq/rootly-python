from typing import Literal, cast

CatalogChecklistTemplateScopeType = Literal["Catalog", "Team"]

CATALOG_CHECKLIST_TEMPLATE_SCOPE_TYPE_VALUES: set[CatalogChecklistTemplateScopeType] = {
    "Catalog",
    "Team",
}


def check_catalog_checklist_template_scope_type(value: str | None) -> CatalogChecklistTemplateScopeType | None:
    if value is None:
        return None
    if value in CATALOG_CHECKLIST_TEMPLATE_SCOPE_TYPE_VALUES:
        return cast(CatalogChecklistTemplateScopeType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOG_CHECKLIST_TEMPLATE_SCOPE_TYPE_VALUES!r}")
