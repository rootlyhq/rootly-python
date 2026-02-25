from typing import Literal, cast

DashboardPanelParamsDatasetsItemGroupByType1Type0Key = Literal["custom_field", "incident_role"]

DASHBOARD_PANEL_PARAMS_DATASETS_ITEM_GROUP_BY_TYPE_1_TYPE_0_KEY_VALUES: set[
    DashboardPanelParamsDatasetsItemGroupByType1Type0Key
] = {
    "custom_field",
    "incident_role",
}


def check_dashboard_panel_params_datasets_item_group_by_type_1_type_0_key(
    value: str | None,
) -> DashboardPanelParamsDatasetsItemGroupByType1Type0Key | None:
    if value is None:
        return None
    if value in DASHBOARD_PANEL_PARAMS_DATASETS_ITEM_GROUP_BY_TYPE_1_TYPE_0_KEY_VALUES:
        return cast(DashboardPanelParamsDatasetsItemGroupByType1Type0Key, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DASHBOARD_PANEL_PARAMS_DATASETS_ITEM_GROUP_BY_TYPE_1_TYPE_0_KEY_VALUES!r}"
    )
