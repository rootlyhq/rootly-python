from typing import Literal

EscalationPolicyPathNotificationTypeRulesItemDeferralWindowRuleType = Literal["deferral_window"]

ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_DEFERRAL_WINDOW_RULE_TYPE_VALUES: set[
    EscalationPolicyPathNotificationTypeRulesItemDeferralWindowRuleType
] = {
    "deferral_window",
}


def check_escalation_policy_path_notification_type_rules_item_deferral_window_rule_type(
    value: str | None,
) -> EscalationPolicyPathNotificationTypeRulesItemDeferralWindowRuleType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_DEFERRAL_WINDOW_RULE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_DEFERRAL_WINDOW_RULE_TYPE_VALUES!r}"
    )
