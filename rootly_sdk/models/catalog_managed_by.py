from typing import Literal

CatalogManagedBy = Literal["admin_web", "api", "backstage", "catalog_sync", "pulumi", "terraform", "web"]

CATALOG_MANAGED_BY_VALUES: set[CatalogManagedBy] = {
    "admin_web",
    "api",
    "backstage",
    "catalog_sync",
    "pulumi",
    "terraform",
    "web",
}


def check_catalog_managed_by(value: str | None) -> CatalogManagedBy | None:
    if value is None:
        return None
    if value in CATALOG_MANAGED_BY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOG_MANAGED_BY_VALUES!r}")
