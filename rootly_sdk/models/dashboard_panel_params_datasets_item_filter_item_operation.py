from typing import Literal, cast

DashboardPanelParamsDatasetsItemFilterItemOperation = Literal["and", "or"]

DASHBOARD_PANEL_PARAMS_DATASETS_ITEM_FILTER_ITEM_OPERATION_VALUES: set[
    DashboardPanelParamsDatasetsItemFilterItemOperation
] = {
    "and",
    "or",
}


def check_dashboard_panel_params_datasets_item_filter_item_operation(
    value: str | None,
) -> DashboardPanelParamsDatasetsItemFilterItemOperation | None:
    if value is None:
        return None
    if value in DASHBOARD_PANEL_PARAMS_DATASETS_ITEM_FILTER_ITEM_OPERATION_VALUES:
        return cast(DashboardPanelParamsDatasetsItemFilterItemOperation, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DASHBOARD_PANEL_PARAMS_DATASETS_ITEM_FILTER_ITEM_OPERATION_VALUES!r}"
    )
