from typing import Literal, cast

BulkDestroyEnvironmentsType1ManagedBy = Literal["api", "backstage", "catalog_sync", "pulumi", "terraform"]

BULK_DESTROY_ENVIRONMENTS_TYPE_1_MANAGED_BY_VALUES: set[BulkDestroyEnvironmentsType1ManagedBy] = {
    "api",
    "backstage",
    "catalog_sync",
    "pulumi",
    "terraform",
}


def check_bulk_destroy_environments_type_1_managed_by(
    value: str | None,
) -> BulkDestroyEnvironmentsType1ManagedBy | None:
    if value is None:
        return None
    if value in BULK_DESTROY_ENVIRONMENTS_TYPE_1_MANAGED_BY_VALUES:
        return cast(BulkDestroyEnvironmentsType1ManagedBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BULK_DESTROY_ENVIRONMENTS_TYPE_1_MANAGED_BY_VALUES!r}"
    )
