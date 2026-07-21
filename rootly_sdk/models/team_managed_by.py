from typing import Literal, cast

TeamManagedBy = Literal["admin_web", "api", "backstage", "catalog_sync", "pulumi", "terraform", "web"]

TEAM_MANAGED_BY_VALUES: set[TeamManagedBy] = {
    "admin_web",
    "api",
    "backstage",
    "catalog_sync",
    "pulumi",
    "terraform",
    "web",
}


def check_team_managed_by(value: str | None) -> TeamManagedBy | None:
    if value is None:
        return None
    if value in TEAM_MANAGED_BY_VALUES:
        return cast(TeamManagedBy, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEAM_MANAGED_BY_VALUES!r}")
