from typing import Literal

ServiceManagedBy = Literal["admin_web", "api", "backstage", "catalog_sync", "pulumi", "terraform", "web"]

SERVICE_MANAGED_BY_VALUES: set[ServiceManagedBy] = {
    "admin_web",
    "api",
    "backstage",
    "catalog_sync",
    "pulumi",
    "terraform",
    "web",
}


def check_service_managed_by(value: str | None) -> ServiceManagedBy | None:
    if value is None:
        return None
    if value in SERVICE_MANAGED_BY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SERVICE_MANAGED_BY_VALUES!r}")
