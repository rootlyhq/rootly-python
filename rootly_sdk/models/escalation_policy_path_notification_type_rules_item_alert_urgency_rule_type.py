from typing import Literal

EscalationPolicyPathNotificationTypeRulesItemAlertUrgencyRuleType = Literal["alert_urgency"]

ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_ALERT_URGENCY_RULE_TYPE_VALUES: set[
    EscalationPolicyPathNotificationTypeRulesItemAlertUrgencyRuleType
] = {
    "alert_urgency",
}


def check_escalation_policy_path_notification_type_rules_item_alert_urgency_rule_type(
    value: str | None,
) -> EscalationPolicyPathNotificationTypeRulesItemAlertUrgencyRuleType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_ALERT_URGENCY_RULE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_ALERT_URGENCY_RULE_TYPE_VALUES!r}"
    )
