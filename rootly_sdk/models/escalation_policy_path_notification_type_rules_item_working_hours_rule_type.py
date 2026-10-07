from typing import Literal

EscalationPolicyPathNotificationTypeRulesItemWorkingHoursRuleType = Literal["working_hour"]

ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_WORKING_HOURS_RULE_TYPE_VALUES: set[
    EscalationPolicyPathNotificationTypeRulesItemWorkingHoursRuleType
] = {
    "working_hour",
}


def check_escalation_policy_path_notification_type_rules_item_working_hours_rule_type(
    value: str | None,
) -> EscalationPolicyPathNotificationTypeRulesItemWorkingHoursRuleType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_WORKING_HOURS_RULE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_WORKING_HOURS_RULE_TYPE_VALUES!r}"
    )
