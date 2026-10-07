from typing import Literal

EnvironmentManagedBy = Literal["admin_web", "api", "backstage", "catalog_sync", "pulumi", "terraform", "web"]

ENVIRONMENT_MANAGED_BY_VALUES: set[EnvironmentManagedBy] = {
    "admin_web",
    "api",
    "backstage",
    "catalog_sync",
    "pulumi",
    "terraform",
    "web",
}


def check_environment_managed_by(value: str | None) -> EnvironmentManagedBy | None:
    if value is None:
        return None
    if value in ENVIRONMENT_MANAGED_BY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENVIRONMENT_MANAGED_BY_VALUES!r}")
