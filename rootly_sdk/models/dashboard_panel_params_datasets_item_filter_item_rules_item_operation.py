from typing import Literal, cast

DashboardPanelParamsDatasetsItemFilterItemRulesItemOperation = Literal["and", "or"]

DASHBOARD_PANEL_PARAMS_DATASETS_ITEM_FILTER_ITEM_RULES_ITEM_OPERATION_VALUES: set[
    DashboardPanelParamsDatasetsItemFilterItemRulesItemOperation
] = {
    "and",
    "or",
}


def check_dashboard_panel_params_datasets_item_filter_item_rules_item_operation(
    value: str | None,
) -> DashboardPanelParamsDatasetsItemFilterItemRulesItemOperation | None:
    if value is None:
        return None
    if value in DASHBOARD_PANEL_PARAMS_DATASETS_ITEM_FILTER_ITEM_RULES_ITEM_OPERATION_VALUES:
        return cast(DashboardPanelParamsDatasetsItemFilterItemRulesItemOperation, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DASHBOARD_PANEL_PARAMS_DATASETS_ITEM_FILTER_ITEM_RULES_ITEM_OPERATION_VALUES!r}"
    )
