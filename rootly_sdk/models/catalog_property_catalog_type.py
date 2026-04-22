from typing import Literal, cast

CatalogPropertyCatalogType = Literal[
    "catalog", "cause", "environment", "functionality", "incident_type", "service", "team"
]

CATALOG_PROPERTY_CATALOG_TYPE_VALUES: set[CatalogPropertyCatalogType] = {
    "catalog",
    "cause",
    "environment",
    "functionality",
    "incident_type",
    "service",
    "team",
}


def check_catalog_property_catalog_type(value: str | None) -> CatalogPropertyCatalogType | None:
    if value is None:
        return None
    if value in CATALOG_PROPERTY_CATALOG_TYPE_VALUES:
        return cast(CatalogPropertyCatalogType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOG_PROPERTY_CATALOG_TYPE_VALUES!r}")
