from typing import Literal, cast

UpdateDashboardPanelDataAttributesParamsDatasetsItemFilterItemOperation = Literal["and", "or"]

UPDATE_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_FILTER_ITEM_OPERATION_VALUES: set[
    UpdateDashboardPanelDataAttributesParamsDatasetsItemFilterItemOperation
] = {
    "and",
    "or",
}


def check_update_dashboard_panel_data_attributes_params_datasets_item_filter_item_operation(
    value: str | None,
) -> UpdateDashboardPanelDataAttributesParamsDatasetsItemFilterItemOperation | None:
    if value is None:
        return None
    if value in UPDATE_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_FILTER_ITEM_OPERATION_VALUES:
        return cast(UpdateDashboardPanelDataAttributesParamsDatasetsItemFilterItemOperation, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_FILTER_ITEM_OPERATION_VALUES!r}"
    )
