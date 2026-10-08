from typing import Literal

EscalationPolicyPathNotificationTypeRulesItemRelatedIncidentsOperator = Literal["is_not_set", "is_set"]

ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_RELATED_INCIDENTS_OPERATOR_VALUES: set[
    EscalationPolicyPathNotificationTypeRulesItemRelatedIncidentsOperator
] = {
    "is_not_set",
    "is_set",
}


def check_escalation_policy_path_notification_type_rules_item_related_incidents_operator(
    value: str | None,
) -> EscalationPolicyPathNotificationTypeRulesItemRelatedIncidentsOperator | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_RELATED_INCIDENTS_OPERATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_RELATED_INCIDENTS_OPERATOR_VALUES!r}"
    )
