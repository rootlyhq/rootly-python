from typing import Literal, cast

NewAlertRoutingRuleDataAttributesConditionType = Literal["all", "any"]

NEW_ALERT_ROUTING_RULE_DATA_ATTRIBUTES_CONDITION_TYPE_VALUES: set[NewAlertRoutingRuleDataAttributesConditionType] = {
    "all",
    "any",
}


def check_new_alert_routing_rule_data_attributes_condition_type(
    value: str | None,
) -> NewAlertRoutingRuleDataAttributesConditionType | None:
    if value is None:
        return None
    if value in NEW_ALERT_ROUTING_RULE_DATA_ATTRIBUTES_CONDITION_TYPE_VALUES:
        return cast(NewAlertRoutingRuleDataAttributesConditionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERT_ROUTING_RULE_DATA_ATTRIBUTES_CONDITION_TYPE_VALUES!r}"
    )
