from typing import Literal, cast

CatalogEntityChecklistStatus = Literal["cancelled", "completed", "in_progress", "triggered"]

CATALOG_ENTITY_CHECKLIST_STATUS_VALUES: set[CatalogEntityChecklistStatus] = {
    "cancelled",
    "completed",
    "in_progress",
    "triggered",
}


def check_catalog_entity_checklist_status(value: str | None) -> CatalogEntityChecklistStatus | None:
    if value is None:
        return None
    if value in CATALOG_ENTITY_CHECKLIST_STATUS_VALUES:
        return cast(CatalogEntityChecklistStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOG_ENTITY_CHECKLIST_STATUS_VALUES!r}")
