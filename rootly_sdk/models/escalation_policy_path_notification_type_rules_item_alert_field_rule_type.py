from typing import Literal

EscalationPolicyPathNotificationTypeRulesItemAlertFieldRuleType = Literal["field"]

ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_ALERT_FIELD_RULE_TYPE_VALUES: set[
    EscalationPolicyPathNotificationTypeRulesItemAlertFieldRuleType
] = {
    "field",
}


def check_escalation_policy_path_notification_type_rules_item_alert_field_rule_type(
    value: str | None,
) -> EscalationPolicyPathNotificationTypeRulesItemAlertFieldRuleType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_ALERT_FIELD_RULE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_ALERT_FIELD_RULE_TYPE_VALUES!r}"
    )
