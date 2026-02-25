from typing import Literal, cast

AlertRoutingRuleConditionType = Literal["all", "any"]

ALERT_ROUTING_RULE_CONDITION_TYPE_VALUES: set[AlertRoutingRuleConditionType] = {
    "all",
    "any",
}


def check_alert_routing_rule_condition_type(value: str | None) -> AlertRoutingRuleConditionType | None:
    if value is None:
        return None
    if value in ALERT_ROUTING_RULE_CONDITION_TYPE_VALUES:
        return cast(AlertRoutingRuleConditionType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_ROUTING_RULE_CONDITION_TYPE_VALUES!r}")
