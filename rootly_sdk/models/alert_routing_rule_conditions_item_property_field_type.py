from typing import Literal, cast

AlertRoutingRuleConditionsItemPropertyFieldType = Literal["attribute", "payload"]

ALERT_ROUTING_RULE_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES: set[AlertRoutingRuleConditionsItemPropertyFieldType] = {
    "attribute",
    "payload",
}


def check_alert_routing_rule_conditions_item_property_field_type(
    value: str | None,
) -> AlertRoutingRuleConditionsItemPropertyFieldType | None:
    if value is None:
        return None
    if value in ALERT_ROUTING_RULE_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES:
        return cast(AlertRoutingRuleConditionsItemPropertyFieldType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_ROUTING_RULE_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES!r}"
    )
