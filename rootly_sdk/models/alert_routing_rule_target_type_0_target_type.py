from typing import Literal, cast

AlertRoutingRuleTargetType0TargetType = Literal["EscalationPolicy", "Group", "Service"]

ALERT_ROUTING_RULE_TARGET_TYPE_0_TARGET_TYPE_VALUES: set[AlertRoutingRuleTargetType0TargetType] = {
    "EscalationPolicy",
    "Group",
    "Service",
}


def check_alert_routing_rule_target_type_0_target_type(value: str | None) -> AlertRoutingRuleTargetType0TargetType | None:
    if value is None:
        return None
    if value in ALERT_ROUTING_RULE_TARGET_TYPE_0_TARGET_TYPE_VALUES:
        return cast(AlertRoutingRuleTargetType0TargetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_ROUTING_RULE_TARGET_TYPE_0_TARGET_TYPE_VALUES!r}"
    )
