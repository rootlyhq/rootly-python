from typing import Literal, cast

UpdateDashboardDataAttributesColor = Literal["#D7F5E1", "#E9E2FF", "#FAE6E8", "#FAEEE6", "#FCF2CF"]

UPDATE_DASHBOARD_DATA_ATTRIBUTES_COLOR_VALUES: set[UpdateDashboardDataAttributesColor] = {
    "#D7F5E1",
    "#E9E2FF",
    "#FAE6E8",
    "#FAEEE6",
    "#FCF2CF",
}


def check_update_dashboard_data_attributes_color(value: str | None) -> UpdateDashboardDataAttributesColor | None:
    if value is None:
        return None
    if value in UPDATE_DASHBOARD_DATA_ATTRIBUTES_COLOR_VALUES:
        return cast(UpdateDashboardDataAttributesColor, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_DASHBOARD_DATA_ATTRIBUTES_COLOR_VALUES!r}")
