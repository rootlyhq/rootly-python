from typing import Literal, cast

DashboardOwner = Literal["team", "user"]

DASHBOARD_OWNER_VALUES: set[DashboardOwner] = {
    "team",
    "user",
}


def check_dashboard_owner(value: str | None) -> DashboardOwner | None:
    if value is None:
        return None
    if value in DASHBOARD_OWNER_VALUES:
        return cast(DashboardOwner, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DASHBOARD_OWNER_VALUES!r}")
