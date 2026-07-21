from typing import Literal, cast

CatalogEntityManagedBy = Literal["admin_web", "api", "backstage", "catalog_sync", "pulumi", "terraform", "web"]

CATALOG_ENTITY_MANAGED_BY_VALUES: set[CatalogEntityManagedBy] = {
    "admin_web",
    "api",
    "backstage",
    "catalog_sync",
    "pulumi",
    "terraform",
    "web",
}


def check_catalog_entity_managed_by(value: str | None) -> CatalogEntityManagedBy | None:
    if value is None:
        return None
    if value in CATALOG_ENTITY_MANAGED_BY_VALUES:
        return cast(CatalogEntityManagedBy, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOG_ENTITY_MANAGED_BY_VALUES!r}")
