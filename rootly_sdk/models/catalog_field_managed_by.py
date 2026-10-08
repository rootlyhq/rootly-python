from typing import Literal

CatalogFieldManagedBy = Literal["admin_web", "api", "backstage", "catalog_sync", "pulumi", "terraform", "web"]

CATALOG_FIELD_MANAGED_BY_VALUES: set[CatalogFieldManagedBy] = {
    "admin_web",
    "api",
    "backstage",
    "catalog_sync",
    "pulumi",
    "terraform",
    "web",
}


def check_catalog_field_managed_by(value: str | None) -> CatalogFieldManagedBy | None:
    if value is None:
        return None
    if value in CATALOG_FIELD_MANAGED_BY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOG_FIELD_MANAGED_BY_VALUES!r}")
