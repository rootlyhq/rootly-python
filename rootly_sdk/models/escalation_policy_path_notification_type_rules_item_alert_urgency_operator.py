from typing import Literal

EscalationPolicyPathNotificationTypeRulesItemAlertUrgencyOperator = Literal[
    "is", "is_not", "is_not_one_of", "is_one_of"
]

ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_ALERT_URGENCY_OPERATOR_VALUES: set[
    EscalationPolicyPathNotificationTypeRulesItemAlertUrgencyOperator
] = {
    "is",
    "is_not",
    "is_not_one_of",
    "is_one_of",
}


def check_escalation_policy_path_notification_type_rules_item_alert_urgency_operator(
    value: str | None,
) -> EscalationPolicyPathNotificationTypeRulesItemAlertUrgencyOperator | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_ALERT_URGENCY_OPERATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_ALERT_URGENCY_OPERATOR_VALUES!r}"
    )
