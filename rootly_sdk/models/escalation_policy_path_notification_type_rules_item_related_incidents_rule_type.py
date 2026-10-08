from typing import Literal

EscalationPolicyPathNotificationTypeRulesItemRelatedIncidentsRuleType = Literal["related_incidents"]

ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_RELATED_INCIDENTS_RULE_TYPE_VALUES: set[
    EscalationPolicyPathNotificationTypeRulesItemRelatedIncidentsRuleType
] = {
    "related_incidents",
}


def check_escalation_policy_path_notification_type_rules_item_related_incidents_rule_type(
    value: str | None,
) -> EscalationPolicyPathNotificationTypeRulesItemRelatedIncidentsRuleType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_RELATED_INCIDENTS_RULE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_RELATED_INCIDENTS_RULE_TYPE_VALUES!r}"
    )
