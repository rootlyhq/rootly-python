from typing import Literal, cast

UpdateDashboardPanelDataAttributesParamsLegendGroups = Literal["all", "charted"]

UPDATE_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_LEGEND_GROUPS_VALUES: set[
    UpdateDashboardPanelDataAttributesParamsLegendGroups
] = {
    "all",
    "charted",
}


def check_update_dashboard_panel_data_attributes_params_legend_groups(
    value: str | None,
) -> UpdateDashboardPanelDataAttributesParamsLegendGroups | None:
    if value is None:
        return None
    if value in UPDATE_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_LEGEND_GROUPS_VALUES:
        return cast(UpdateDashboardPanelDataAttributesParamsLegendGroups, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_LEGEND_GROUPS_VALUES!r}"
    )
