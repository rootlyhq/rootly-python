from typing import Literal, cast

UpdateAlertRoutingRuleDataType = Literal["alert_routing_rules"]

UPDATE_ALERT_ROUTING_RULE_DATA_TYPE_VALUES: set[UpdateAlertRoutingRuleDataType] = {
    "alert_routing_rules",
}


def check_update_alert_routing_rule_data_type(value: str | None) -> UpdateAlertRoutingRuleDataType | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_ROUTING_RULE_DATA_TYPE_VALUES:
        return cast(UpdateAlertRoutingRuleDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_ROUTING_RULE_DATA_TYPE_VALUES!r}")
