from typing import Literal, cast

NewDashboardPanelDataAttributesParamsLegendGroups = Literal["all", "charted"]

NEW_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_LEGEND_GROUPS_VALUES: set[
    NewDashboardPanelDataAttributesParamsLegendGroups
] = {
    "all",
    "charted",
}


def check_new_dashboard_panel_data_attributes_params_legend_groups(
    value: str | None,
) -> NewDashboardPanelDataAttributesParamsLegendGroups | None:
    if value is None:
        return None
    if value in NEW_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_LEGEND_GROUPS_VALUES:
        return cast(NewDashboardPanelDataAttributesParamsLegendGroups, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_LEGEND_GROUPS_VALUES!r}"
    )
