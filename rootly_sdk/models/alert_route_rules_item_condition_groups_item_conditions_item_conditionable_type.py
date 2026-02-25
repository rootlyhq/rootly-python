from typing import Literal, cast

AlertRouteRulesItemConditionGroupsItemConditionsItemConditionableType = Literal["AlertField"]

ALERT_ROUTE_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES: set[
    AlertRouteRulesItemConditionGroupsItemConditionsItemConditionableType
] = {
    "AlertField",
}


def check_alert_route_rules_item_condition_groups_item_conditions_item_conditionable_type(
    value: str | None,
) -> AlertRouteRulesItemConditionGroupsItemConditionsItemConditionableType | None:
    if value is None:
        return None
    if value in ALERT_ROUTE_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES:
        return cast(AlertRouteRulesItemConditionGroupsItemConditionsItemConditionableType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_ROUTE_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES!r}"
    )
