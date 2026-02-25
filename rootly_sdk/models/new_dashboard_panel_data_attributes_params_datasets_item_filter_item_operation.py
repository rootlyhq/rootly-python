from typing import Literal, cast

NewDashboardPanelDataAttributesParamsDatasetsItemFilterItemOperation = Literal["and", "or"]

NEW_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_FILTER_ITEM_OPERATION_VALUES: set[
    NewDashboardPanelDataAttributesParamsDatasetsItemFilterItemOperation
] = {
    "and",
    "or",
}


def check_new_dashboard_panel_data_attributes_params_datasets_item_filter_item_operation(
    value: str | None,
) -> NewDashboardPanelDataAttributesParamsDatasetsItemFilterItemOperation | None:
    if value is None:
        return None
    if value in NEW_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_FILTER_ITEM_OPERATION_VALUES:
        return cast(NewDashboardPanelDataAttributesParamsDatasetsItemFilterItemOperation, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_FILTER_ITEM_OPERATION_VALUES!r}"
    )
