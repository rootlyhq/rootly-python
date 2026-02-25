from typing import Literal, cast

AlertRoutingRuleConditionPropertyFieldType = Literal["attribute", "payload"]

ALERT_ROUTING_RULE_CONDITION_PROPERTY_FIELD_TYPE_VALUES: set[AlertRoutingRuleConditionPropertyFieldType] = {
    "attribute",
    "payload",
}


def check_alert_routing_rule_condition_property_field_type(
    value: str | None,
) -> AlertRoutingRuleConditionPropertyFieldType | None:
    if value is None:
        return None
    if value in ALERT_ROUTING_RULE_CONDITION_PROPERTY_FIELD_TYPE_VALUES:
        return cast(AlertRoutingRuleConditionPropertyFieldType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_ROUTING_RULE_CONDITION_PROPERTY_FIELD_TYPE_VALUES!r}"
    )
