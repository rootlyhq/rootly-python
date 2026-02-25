from typing import Literal, cast

NewDashboardDataAttributesOwner = Literal["team", "user"]

NEW_DASHBOARD_DATA_ATTRIBUTES_OWNER_VALUES: set[NewDashboardDataAttributesOwner] = {
    "team",
    "user",
}


def check_new_dashboard_data_attributes_owner(value: str | None) -> NewDashboardDataAttributesOwner | None:
    if value is None:
        return None
    if value in NEW_DASHBOARD_DATA_ATTRIBUTES_OWNER_VALUES:
        return cast(NewDashboardDataAttributesOwner, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_DASHBOARD_DATA_ATTRIBUTES_OWNER_VALUES!r}")
