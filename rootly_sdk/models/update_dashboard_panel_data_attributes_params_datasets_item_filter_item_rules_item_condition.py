from typing import Literal, cast

UpdateDashboardPanelDataAttributesParamsDatasetsItemFilterItemRulesItemCondition = Literal[
    "!=", "<=", "=", ">=", "assigned", "contains", "exists", "not_contains", "not_exists", "unassigned"
]

UPDATE_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_FILTER_ITEM_RULES_ITEM_CONDITION_VALUES: set[
    UpdateDashboardPanelDataAttributesParamsDatasetsItemFilterItemRulesItemCondition
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


def check_update_dashboard_panel_data_attributes_params_datasets_item_filter_item_rules_item_condition(
    value: str | None,
) -> UpdateDashboardPanelDataAttributesParamsDatasetsItemFilterItemRulesItemCondition | None:
    if value is None:
        return None
    if value in UPDATE_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_FILTER_ITEM_RULES_ITEM_CONDITION_VALUES:
        return cast(UpdateDashboardPanelDataAttributesParamsDatasetsItemFilterItemRulesItemCondition, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_FILTER_ITEM_RULES_ITEM_CONDITION_VALUES!r}"
    )
