from typing import Literal, cast

CatalogFieldCatalogType = Literal[
    "catalog", "cause", "environment", "functionality", "incident_type", "service", "team"
]

CATALOG_FIELD_CATALOG_TYPE_VALUES: set[CatalogFieldCatalogType] = {
    "catalog",
    "cause",
    "environment",
    "functionality",
    "incident_type",
    "service",
    "team",
}


def check_catalog_field_catalog_type(value: str | None) -> CatalogFieldCatalogType | None:
    if value is None:
        return None
    if value in CATALOG_FIELD_CATALOG_TYPE_VALUES:
        return cast(CatalogFieldCatalogType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOG_FIELD_CATALOG_TYPE_VALUES!r}")
