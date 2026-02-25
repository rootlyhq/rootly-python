from typing import Literal, cast

DashboardPanelParamsDatasetsItemFilterItemRulesItemCondition = Literal[
    "!=", "<=", "=", ">=", "assigned", "contains", "exists", "not_contains", "not_exists", "unassigned"
]

DASHBOARD_PANEL_PARAMS_DATASETS_ITEM_FILTER_ITEM_RULES_ITEM_CONDITION_VALUES: set[
    DashboardPanelParamsDatasetsItemFilterItemRulesItemCondition
] = {
    "!=",
    "<=",
    "=",
    ">=",
    "assigned",
    "contains",
    "exists",
    "not_contains",
    "not_exists",
    "unassigned",
}


def check_dashboard_panel_params_datasets_item_filter_item_rules_item_condition(
    value: str | None,
) -> DashboardPanelParamsDatasetsItemFilterItemRulesItemCondition | None:
    if value is None:
        return None
    if value in DASHBOARD_PANEL_PARAMS_DATASETS_ITEM_FILTER_ITEM_RULES_ITEM_CONDITION_VALUES:
        return cast(DashboardPanelParamsDatasetsItemFilterItemRulesItemCondition, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DASHBOARD_PANEL_PARAMS_DATASETS_ITEM_FILTER_ITEM_RULES_ITEM_CONDITION_VALUES!r}"
    )
