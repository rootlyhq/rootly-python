from typing import Literal, cast

UpdateAlertRoutingRuleDataAttributesConditionType = Literal["all", "any"]

UPDATE_ALERT_ROUTING_RULE_DATA_ATTRIBUTES_CONDITION_TYPE_VALUES: set[
    UpdateAlertRoutingRuleDataAttributesConditionType
] = {
    "all",
    "any",
}


def check_update_alert_routing_rule_data_attributes_condition_type(
    value: str | None,
) -> UpdateAlertRoutingRuleDataAttributesConditionType | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_ROUTING_RULE_DATA_ATTRIBUTES_CONDITION_TYPE_VALUES:
        return cast(UpdateAlertRoutingRuleDataAttributesConditionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_ROUTING_RULE_DATA_ATTRIBUTES_CONDITION_TYPE_VALUES!r}"
    )
