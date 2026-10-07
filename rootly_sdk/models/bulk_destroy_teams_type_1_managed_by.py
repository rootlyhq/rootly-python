from typing import Literal

BulkDestroyTeamsType1ManagedBy = Literal["api", "backstage", "catalog_sync", "pulumi", "terraform"]

BULK_DESTROY_TEAMS_TYPE_1_MANAGED_BY_VALUES: set[BulkDestroyTeamsType1ManagedBy] = {
    "api",
    "backstage",
    "catalog_sync",
    "pulumi",
    "terraform",
}


def check_bulk_destroy_teams_type_1_managed_by(value: str | None) -> BulkDestroyTeamsType1ManagedBy | None:
    if value is None:
        return None
    if value in BULK_DESTROY_TEAMS_TYPE_1_MANAGED_BY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BULK_DESTROY_TEAMS_TYPE_1_MANAGED_BY_VALUES!r}")
