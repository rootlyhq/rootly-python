from typing import Literal

NewAlertRoutingRuleDataAttributesDestinationTargetType = Literal[
    "EscalationPolicy", "Functionality", "Group", "Service"
]

NEW_ALERT_ROUTING_RULE_DATA_ATTRIBUTES_DESTINATION_TARGET_TYPE_VALUES: set[
    NewAlertRoutingRuleDataAttributesDestinationTargetType
] = {
    "EscalationPolicy",
    "Functionality",
    "Group",
    "Service",
}


def check_new_alert_routing_rule_data_attributes_destination_target_type(
    value: str | None,
) -> NewAlertRoutingRuleDataAttributesDestinationTargetType | None:
    if value is None:
        return None
    if value in NEW_ALERT_ROUTING_RULE_DATA_ATTRIBUTES_DESTINATION_TARGET_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERT_ROUTING_RULE_DATA_ATTRIBUTES_DESTINATION_TARGET_TYPE_VALUES!r}"
    )
