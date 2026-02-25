from typing import Literal, cast

NewAlertRoutingRuleDataType = Literal["alert_routing_rules"]

NEW_ALERT_ROUTING_RULE_DATA_TYPE_VALUES: set[NewAlertRoutingRuleDataType] = {
    "alert_routing_rules",
}


def check_new_alert_routing_rule_data_type(value: str | None) -> NewAlertRoutingRuleDataType | None:
    if value is None:
        return None
    if value in NEW_ALERT_ROUTING_RULE_DATA_TYPE_VALUES:
        return cast(NewAlertRoutingRuleDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_ALERT_ROUTING_RULE_DATA_TYPE_VALUES!r}")
