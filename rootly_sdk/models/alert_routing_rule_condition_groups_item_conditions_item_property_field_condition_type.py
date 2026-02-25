from typing import Literal, cast

AlertRoutingRuleConditionGroupsItemConditionsItemPropertyFieldConditionType = Literal[
    "contains",
    "does_not_contain",
    "ends_with",
    "is_empty",
    "is_not_one_of",
    "is_one_of",
    "matches_regex",
    "starts_with",
]

ALERT_ROUTING_RULE_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_PROPERTY_FIELD_CONDITION_TYPE_VALUES: set[
    AlertRoutingRuleConditionGroupsItemConditionsItemPropertyFieldConditionType
] = {
    "contains",
    "does_not_contain",
    "ends_with",
    "is_empty",
    "is_not_one_of",
    "is_one_of",
    "matches_regex",
    "starts_with",
}


def check_alert_routing_rule_condition_groups_item_conditions_item_property_field_condition_type(
    value: str | None,
) -> AlertRoutingRuleConditionGroupsItemConditionsItemPropertyFieldConditionType | None:
    if value is None:
        return None
    if value in ALERT_ROUTING_RULE_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_PROPERTY_FIELD_CONDITION_TYPE_VALUES:
        return cast(AlertRoutingRuleConditionGroupsItemConditionsItemPropertyFieldConditionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_ROUTING_RULE_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_PROPERTY_FIELD_CONDITION_TYPE_VALUES!r}"
    )
