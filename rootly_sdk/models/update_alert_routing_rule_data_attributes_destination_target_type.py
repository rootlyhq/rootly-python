from typing import Literal, cast

UpdateAlertRoutingRuleDataAttributesDestinationTargetType = Literal["EscalationPolicy", "Group", "Service"]

UPDATE_ALERT_ROUTING_RULE_DATA_ATTRIBUTES_DESTINATION_TARGET_TYPE_VALUES: set[
    UpdateAlertRoutingRuleDataAttributesDestinationTargetType
] = {
    "EscalationPolicy",
    "Group",
    "Service",
}


def check_update_alert_routing_rule_data_attributes_destination_target_type(
    value: str | None,
) -> UpdateAlertRoutingRuleDataAttributesDestinationTargetType | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_ROUTING_RULE_DATA_ATTRIBUTES_DESTINATION_TARGET_TYPE_VALUES:
        return cast(UpdateAlertRoutingRuleDataAttributesDestinationTargetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_ROUTING_RULE_DATA_ATTRIBUTES_DESTINATION_TARGET_TYPE_VALUES!r}"
    )
