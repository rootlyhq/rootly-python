from typing import Literal, cast

UpdateDashboardPanelDataAttributesParamsDatasetsItemGroupByType1Type0Key = Literal["custom_field", "incident_role"]

UPDATE_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_GROUP_BY_TYPE_1_TYPE_0_KEY_VALUES: set[
    UpdateDashboardPanelDataAttributesParamsDatasetsItemGroupByType1Type0Key
] = {
    "custom_field",
    "incident_role",
}


def check_update_dashboard_panel_data_attributes_params_datasets_item_group_by_type_1_type_0_key(
    value: str | None,
) -> UpdateDashboardPanelDataAttributesParamsDatasetsItemGroupByType1Type0Key | None:
    if value is None:
        return None
    if value in UPDATE_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_GROUP_BY_TYPE_1_TYPE_0_KEY_VALUES:
        return cast(UpdateDashboardPanelDataAttributesParamsDatasetsItemGroupByType1Type0Key, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_GROUP_BY_TYPE_1_TYPE_0_KEY_VALUES!r}"
    )
