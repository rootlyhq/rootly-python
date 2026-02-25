from typing import Literal, cast

AlertRouteRulesItemConditionGroupsItemConditionsItemPropertyFieldType = Literal["alert_field", "attribute", "payload"]

ALERT_ROUTE_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES: set[
    AlertRouteRulesItemConditionGroupsItemConditionsItemPropertyFieldType
] = {
    "alert_field",
    "attribute",
    "payload",
}


def check_alert_route_rules_item_condition_groups_item_conditions_item_property_field_type(
    value: str | None,
) -> AlertRouteRulesItemConditionGroupsItemConditionsItemPropertyFieldType | None:
    if value is None:
        return None
    if value in ALERT_ROUTE_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES:
        return cast(AlertRouteRulesItemConditionGroupsItemConditionsItemPropertyFieldType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_ROUTE_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES!r}"
    )
