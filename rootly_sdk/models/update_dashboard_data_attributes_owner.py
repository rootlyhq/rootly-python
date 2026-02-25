from typing import Literal, cast

UpdateDashboardDataAttributesOwner = Literal["team", "user"]

UPDATE_DASHBOARD_DATA_ATTRIBUTES_OWNER_VALUES: set[UpdateDashboardDataAttributesOwner] = {
    "team",
    "user",
}


def check_update_dashboard_data_attributes_owner(value: str | None) -> UpdateDashboardDataAttributesOwner | None:
    if value is None:
        return None
    if value in UPDATE_DASHBOARD_DATA_ATTRIBUTES_OWNER_VALUES:
        return cast(UpdateDashboardDataAttributesOwner, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_DASHBOARD_DATA_ATTRIBUTES_OWNER_VALUES!r}")
