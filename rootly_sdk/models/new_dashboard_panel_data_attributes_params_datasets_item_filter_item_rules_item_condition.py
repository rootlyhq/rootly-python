from typing import Literal, cast

NewDashboardPanelDataAttributesParamsDatasetsItemFilterItemRulesItemCondition = Literal[
    "!=", "<=", "=", ">=", "assigned", "contains", "exists", "not_contains", "not_exists", "unassigned"
]

NEW_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_FILTER_ITEM_RULES_ITEM_CONDITION_VALUES: set[
    NewDashboardPanelDataAttributesParamsDatasetsItemFilterItemRulesItemCondition
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


def check_new_dashboard_panel_data_attributes_params_datasets_item_filter_item_rules_item_condition(
    value: str | None,
) -> NewDashboardPanelDataAttributesParamsDatasetsItemFilterItemRulesItemCondition | None:
    if value is None:
        return None
    if value in NEW_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_FILTER_ITEM_RULES_ITEM_CONDITION_VALUES:
        return cast(NewDashboardPanelDataAttributesParamsDatasetsItemFilterItemRulesItemCondition, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_FILTER_ITEM_RULES_ITEM_CONDITION_VALUES!r}"
    )
