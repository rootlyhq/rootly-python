from typing import Literal

BulkDestroyServicesType1ManagedBy = Literal["api", "backstage", "catalog_sync", "pulumi", "terraform"]

BULK_DESTROY_SERVICES_TYPE_1_MANAGED_BY_VALUES: set[BulkDestroyServicesType1ManagedBy] = {
    "api",
    "backstage",
    "catalog_sync",
    "pulumi",
    "terraform",
}


def check_bulk_destroy_services_type_1_managed_by(value: str | None) -> BulkDestroyServicesType1ManagedBy | None:
    if value is None:
        return None
    if value in BULK_DESTROY_SERVICES_TYPE_1_MANAGED_BY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BULK_DESTROY_SERVICES_TYPE_1_MANAGED_BY_VALUES!r}")
