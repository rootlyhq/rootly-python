from typing import Literal, cast

CatalogPropertyManagedBy = Literal["admin_web", "api", "backstage", "catalog_sync", "pulumi", "terraform", "web"]

CATALOG_PROPERTY_MANAGED_BY_VALUES: set[CatalogPropertyManagedBy] = {
    "admin_web",
    "api",
    "backstage",
    "catalog_sync",
    "pulumi",
    "terraform",
    "web",
}


def check_catalog_property_managed_by(value: str | None) -> CatalogPropertyManagedBy | None:
    if value is None:
        return None
    if value in CATALOG_PROPERTY_MANAGED_BY_VALUES:
        return cast(CatalogPropertyManagedBy, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOG_PROPERTY_MANAGED_BY_VALUES!r}")
