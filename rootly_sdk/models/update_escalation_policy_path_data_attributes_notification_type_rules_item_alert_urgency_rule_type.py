from typing import Literal

UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgencyRuleType = Literal["alert_urgency"]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_ALERT_URGENCY_RULE_TYPE_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgencyRuleType
] = {
    "alert_urgency",
}


def check_update_escalation_policy_path_data_attributes_notification_type_rules_item_alert_urgency_rule_type(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgencyRuleType | None:
    if value is None:
        return None
    if (
        value
        in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_ALERT_URGENCY_RULE_TYPE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_ALERT_URGENCY_RULE_TYPE_VALUES!r}"
    )
