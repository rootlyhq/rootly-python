from typing import Literal, cast

NewDashboardDataAttributesColor = Literal["#D7F5E1", "#E9E2FF", "#FAE6E8", "#FAEEE6", "#FCF2CF"]

NEW_DASHBOARD_DATA_ATTRIBUTES_COLOR_VALUES: set[NewDashboardDataAttributesColor] = {
    "#D7F5E1",
    "#E9E2FF",
    "#FAE6E8",
    "#FAEEE6",
    "#FCF2CF",
}


def check_new_dashboard_data_attributes_color(value: str | None) -> NewDashboardDataAttributesColor | None:
    if value is None:
        return None
    if value in NEW_DASHBOARD_DATA_ATTRIBUTES_COLOR_VALUES:
        return cast(NewDashboardDataAttributesColor, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_DASHBOARD_DATA_ATTRIBUTES_COLOR_VALUES!r}")
