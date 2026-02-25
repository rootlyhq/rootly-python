from typing import Literal, cast

AlertRoutingRuleResponseDataType = Literal["alert_routing_rules"]

ALERT_ROUTING_RULE_RESPONSE_DATA_TYPE_VALUES: set[AlertRoutingRuleResponseDataType] = {
    "alert_routing_rules",
}


def check_alert_routing_rule_response_data_type(value: str | None) -> AlertRoutingRuleResponseDataType | None:
    if value is None:
        return None
    if value in ALERT_ROUTING_RULE_RESPONSE_DATA_TYPE_VALUES:
        return cast(AlertRoutingRuleResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_ROUTING_RULE_RESPONSE_DATA_TYPE_VALUES!r}")
