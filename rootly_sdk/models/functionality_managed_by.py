from typing import Literal

FunctionalityManagedBy = Literal["admin_web", "api", "backstage", "catalog_sync", "pulumi", "terraform", "web"]

FUNCTIONALITY_MANAGED_BY_VALUES: set[FunctionalityManagedBy] = {
    "admin_web",
    "api",
    "backstage",
    "catalog_sync",
    "pulumi",
    "terraform",
    "web",
}


def check_functionality_managed_by(value: str | None) -> FunctionalityManagedBy | None:
    if value is None:
        return None
    if value in FUNCTIONALITY_MANAGED_BY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FUNCTIONALITY_MANAGED_BY_VALUES!r}")
