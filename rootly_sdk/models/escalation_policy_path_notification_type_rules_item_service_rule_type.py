from typing import Literal

EscalationPolicyPathNotificationTypeRulesItemServiceRuleType = Literal["service"]

ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_SERVICE_RULE_TYPE_VALUES: set[
    EscalationPolicyPathNotificationTypeRulesItemServiceRuleType
] = {
    "service",
}


def check_escalation_policy_path_notification_type_rules_item_service_rule_type(
    value: str | None,
) -> EscalationPolicyPathNotificationTypeRulesItemServiceRuleType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_SERVICE_RULE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_SERVICE_RULE_TYPE_VALUES!r}"
    )
