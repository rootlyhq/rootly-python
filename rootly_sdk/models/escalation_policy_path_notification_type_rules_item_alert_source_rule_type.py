from typing import Literal

EscalationPolicyPathNotificationTypeRulesItemAlertSourceRuleType = Literal["source"]

ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_ALERT_SOURCE_RULE_TYPE_VALUES: set[
    EscalationPolicyPathNotificationTypeRulesItemAlertSourceRuleType
] = {
    "source",
}


def check_escalation_policy_path_notification_type_rules_item_alert_source_rule_type(
    value: str | None,
) -> EscalationPolicyPathNotificationTypeRulesItemAlertSourceRuleType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_ALERT_SOURCE_RULE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_ALERT_SOURCE_RULE_TYPE_VALUES!r}"
    )
