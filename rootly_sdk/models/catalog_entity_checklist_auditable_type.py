from typing import Literal, cast

CatalogEntityChecklistAuditableType = Literal[
    "CatalogEntity", "Cause", "Environment", "Functionality", "Group", "IncidentType", "Service"
]

CATALOG_ENTITY_CHECKLIST_AUDITABLE_TYPE_VALUES: set[CatalogEntityChecklistAuditableType] = {
    "CatalogEntity",
    "Cause",
    "Environment",
    "Functionality",
    "Group",
    "IncidentType",
    "Service",
}


def check_catalog_entity_checklist_auditable_type(value: str | None) -> CatalogEntityChecklistAuditableType | None:
    if value is None:
        return None
    if value in CATALOG_ENTITY_CHECKLIST_AUDITABLE_TYPE_VALUES:
        return cast(CatalogEntityChecklistAuditableType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOG_ENTITY_CHECKLIST_AUDITABLE_TYPE_VALUES!r}")
