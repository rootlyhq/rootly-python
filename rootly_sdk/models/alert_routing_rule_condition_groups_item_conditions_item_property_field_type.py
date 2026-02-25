from typing import Literal, cast

AlertRoutingRuleConditionGroupsItemConditionsItemPropertyFieldType = Literal["attribute", "payload"]

ALERT_ROUTING_RULE_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES: set[
    AlertRoutingRuleConditionGroupsItemConditionsItemPropertyFieldType
] = {
    "attribute",
    "payload",
}


def check_alert_routing_rule_condition_groups_item_conditions_item_property_field_type(
    value: str | None,
) -> AlertRoutingRuleConditionGroupsItemConditionsItemPropertyFieldType | None:
    if value is None:
        return None
    if value in ALERT_ROUTING_RULE_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES:
        return cast(AlertRoutingRuleConditionGroupsItemConditionsItemPropertyFieldType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_ROUTING_RULE_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES!r}"
    )
