from typing import Literal

BulkDestroyCatalogEntitiesType1ManagedBy = Literal["api", "backstage", "catalog_sync", "pulumi", "terraform"]

BULK_DESTROY_CATALOG_ENTITIES_TYPE_1_MANAGED_BY_VALUES: set[BulkDestroyCatalogEntitiesType1ManagedBy] = {
    "api",
    "backstage",
    "catalog_sync",
    "pulumi",
    "terraform",
}


def check_bulk_destroy_catalog_entities_type_1_managed_by(
    value: str | None,
) -> BulkDestroyCatalogEntitiesType1ManagedBy | None:
    if value is None:
        return None
    if value in BULK_DESTROY_CATALOG_ENTITIES_TYPE_1_MANAGED_BY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BULK_DESTROY_CATALOG_ENTITIES_TYPE_1_MANAGED_BY_VALUES!r}"
    )
